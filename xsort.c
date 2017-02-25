#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
int main(int argc, char * argv[])
{
  char *filename=(char *)malloc(20*sizeof(char));
  if(argc!=2)
  {
    printf("The correct usage is %s <filename> \n", argv[0]);
    exit(1);
  }
  else
  {

    strcpy(filename,argv[1]);
  }
  pid_t pid = fork();
  if(pid==0)
  {
    char* argv[6];
  //  char* file=(char *)malloc(20*sizeof(char));
//    file = strcat("./sort 1 ",filename);
//    printf("%s", file)
    char file[] = "./sort1 ";
    strcat(file,filename);
    strcat(file,";bash\0");
    argv[0]=(char *)malloc(10*sizeof(char)); strcpy(argv[0],"xterm");
    argv[1]=(char *)malloc(10*sizeof(char)); strcpy(argv[1],"-e");
    argv[2]=(char *)malloc(20*sizeof(char)); strcpy(argv[2],file); // Note: works with "./sort1 file.txt;bash"
    argv[3]=NULL;
//    execlp("xterm","xterm","-e","./sort1 file.txt","127.0.0.1",(char *) 0);
    execvp(argv[0], argv);
  //h  printf("execvp failed %s \n", strerror(errno));

  }
  else if(pid>0)
  {
//    printf("Parent Process\n");
  }
  else
  {
    printf("Fork failed\n");
  }
//
wait(2);
printf("Finishing");
}
