/*
 * System Information Utility
 * Displays comprehensive system information on Linux
 *
 * Author: Angelina Botez
 * License: GNU General Public License v3.0
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/utsname.h>
#include <sys/sysinfo.h>
#include <time.h>
#include <pwd.h>

#define VERSION "1.0"

// Function prototypes
void print_header(void);
void print_os_info(void);
void print_cpu_info(void);
void print_memory_info(void);
void print_uptime_info(void);
void print_user_info(void);
void print_disk_info(void);
void format_bytes(unsigned long bytes, char *buffer, size_t buffer_size);
void format_uptime(long uptime, char *buffer, size_t buffer_size);

int main(int argc, char *argv[]) {
    // Check for help flag
    if (argc > 1 && (strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0)) {
        printf("System Information Utility v%s\n", VERSION);
        printf("Usage: %s [options]\n", argv[0]);
        printf("Options:\n");
        printf("  -h, --help     Show this help message\n");
        printf("  -v, --version  Show version information\n");
        return 0;
    }

    // Check for version flag
    if (argc > 1 && (strcmp(argv[1], "-v") == 0 || strcmp(argv[1], "--version") == 0)) {
        printf("System Information Utility v%s\n", VERSION);
        printf("License: GNU General Public License v3.0\n");
        return 0;
    }

    print_header();
    print_os_info();
    print_user_info();
    print_cpu_info();
    print_memory_info();
    print_uptime_info();
    print_disk_info();

    return 0;
}

void print_header(void) {
    printf("========================================\n");
    printf("    SYSTEM INFORMATION UTILITY v%s\n", VERSION);
    printf("========================================\n\n");
}

void print_os_info(void) {
    struct utsname sys_info;

    if (uname(&sys_info) != 0) {
        perror("uname");
        return;
    }

    printf("Operating System Information:\n");
    printf("  System Name:    %s\n", sys_info.sysname);
    printf("  Node Name:      %s\n", sys_info.nodename);
    printf("  Release:        %s\n", sys_info.release);
    printf("  Version:        %s\n", sys_info.version);
    printf("  Machine:        %s\n", sys_info.machine);
    printf("\n");
}

void print_cpu_info(void) {
    FILE *fp;
    char line[256];
    char cpu_model[256] = "Unknown";
    int cpu_count = 0;

    printf("CPU Information:\n");

    fp = fopen("/proc/cpuinfo", "r");
    if (fp != NULL) {
        while (fgets(line, sizeof(line), fp)) {
            if (strncmp(line, "model name", 10) == 0) {
                char *colon = strchr(line, ':');
                if (colon != NULL) {
                    colon += 2; // Skip ": "
                    // Remove newline
                    size_t len = strlen(colon);
                    if (len > 0 && colon[len-1] == '\n') {
                        colon[len-1] = '\0';
                    }
                    strncpy(cpu_model, colon, sizeof(cpu_model) - 1);
                    cpu_count++;
                }
            }
        }
        fclose(fp);

        printf("  Model:          %s\n", cpu_model);
        printf("  CPU Cores:      %d\n", cpu_count);
    } else {
        printf("  Unable to read CPU information\n");
    }

    printf("\n");
}

void print_memory_info(void) {
    struct sysinfo sys_info;
    char total_ram[64], free_ram[64], used_ram[64];
    char total_swap[64], free_swap[64];

    if (sysinfo(&sys_info) != 0) {
        perror("sysinfo");
        return;
    }

    unsigned long total_memory = sys_info.totalram * sys_info.mem_unit;
    unsigned long free_memory = sys_info.freeram * sys_info.mem_unit;
    unsigned long used_memory = total_memory - free_memory;
    unsigned long total_swap_mem = sys_info.totalswap * sys_info.mem_unit;
    unsigned long free_swap_mem = sys_info.freeswap * sys_info.mem_unit;

    format_bytes(total_memory, total_ram, sizeof(total_ram));
    format_bytes(free_memory, free_ram, sizeof(free_ram));
    format_bytes(used_memory, used_ram, sizeof(used_ram));
    format_bytes(total_swap_mem, total_swap, sizeof(total_swap));
    format_bytes(free_swap_mem, free_swap, sizeof(free_swap));

    printf("Memory Information:\n");
    printf("  Total RAM:      %s\n", total_ram);
    printf("  Used RAM:       %s\n", used_ram);
    printf("  Free RAM:       %s\n", free_ram);
    printf("  Total Swap:     %s\n", total_swap);
    printf("  Free Swap:      %s\n", free_swap);
    printf("\n");
}

void print_uptime_info(void) {
    struct sysinfo sys_info;
    char uptime_str[128];

    if (sysinfo(&sys_info) != 0) {
        perror("sysinfo");
        return;
    }

    format_uptime(sys_info.uptime, uptime_str, sizeof(uptime_str));

    printf("System Uptime:\n");
    printf("  Uptime:         %s\n", uptime_str);
    printf("  Processes:      %d\n", sys_info.procs);
    printf("\n");
}

void print_user_info(void) {
    char *username = getenv("USER");
    char hostname[256];
    uid_t uid = getuid();
    struct passwd *pw = getpwuid(uid);

    gethostname(hostname, sizeof(hostname));

    printf("User Information:\n");
    if (username != NULL) {
        printf("  Username:       %s\n", username);
    }
    if (pw != NULL) {
        printf("  User ID:        %d\n", uid);
        printf("  Home Directory: %s\n", pw->pw_dir);
        printf("  Shell:          %s\n", pw->pw_shell);
    }
    printf("  Hostname:       %s\n", hostname);
    printf("\n");
}

void print_disk_info(void) {
    FILE *fp;
    char line[512];

    printf("Disk Usage (mounted filesystems):\n");

    fp = popen("df -h --output=source,size,used,avail,pcent,target -x tmpfs -x devtmpfs 2>/dev/null", "r");
    if (fp != NULL) {
        // Print the output from df command
        int first_line = 1;
        while (fgets(line, sizeof(line), fp)) {
            if (first_line) {
                printf("  %s", line);
                first_line = 0;
            } else {
                printf("  %s", line);
            }
        }
        pclose(fp);
    } else {
        printf("  Unable to read disk information\n");
    }

    printf("\n");
}

void format_bytes(unsigned long bytes, char *buffer, size_t buffer_size) {
    const char *units[] = {"B", "KB", "MB", "GB", "TB"};
    int unit_index = 0;
    double size = (double)bytes;

    while (size >= 1024.0 && unit_index < 4) {
        size /= 1024.0;
        unit_index++;
    }

    snprintf(buffer, buffer_size, "%.2f %s", size, units[unit_index]);
}

void format_uptime(long uptime, char *buffer, size_t buffer_size) {
    int days = uptime / 86400;
    int hours = (uptime % 86400) / 3600;
    int minutes = (uptime % 3600) / 60;
    int seconds = uptime % 60;

    if (days > 0) {
        snprintf(buffer, buffer_size, "%d days, %d hours, %d minutes, %d seconds",
                 days, hours, minutes, seconds);
    } else if (hours > 0) {
        snprintf(buffer, buffer_size, "%d hours, %d minutes, %d seconds",
                 hours, minutes, seconds);
    } else if (minutes > 0) {
        snprintf(buffer, buffer_size, "%d minutes, %d seconds",
                 minutes, seconds);
    } else {
        snprintf(buffer, buffer_size, "%d seconds", seconds);
    }
}
