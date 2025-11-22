#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main() {
	while (1) {
		pid_t pid = fork();
		if (pid == 0) {
			execlp("wine", "wine", "svr.exe", NULL);
		} else if (pid > 0) {
			int status;
			waitpid(pid, &status, 0);
		}
	} 
	return 0;
}
