#include <stdio.h> 
#include <stdlib.h> 
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <time.h>
// Edit this value
#define LIMIT 10


sem_t semP, semC;




const int limit = LIMIT;


int buffer[LIMIT];
int counter = 0;

FILE *file;

int randomrange(int min, int max){
    
   return min + rand() / (RAND_MAX / (max - min + 1) + 1);
}

void *producer(void *arg) {
    

    for (int i = 0; i < limit; i++) {

        while(counter == limit){
            printf("Production on wait, buffer is full. \n");
            sem_wait(&semC);
            printf("Production continues. \n");
        }

        // producer delay set to : 5
        sleep(5);   
        counter++;
        srand(time(0));
        int randnum = randomrange(0,100);
        buffer[counter - 1] =  randnum;
        sem_post(&semP);
        printf("Producer Job Finished. \n");

    }
 }

void *consumer(void *arg) {

    for (int i = 0; i < limit; i++) {

        while(counter == 0){
            printf("Consumer waiting, buffer is empty. \n");
            sem_wait(&semP);
            printf("Consumer continues. \n");
        }

        //consumer delay set to : 2
        sleep(2);   
        counter--;
        int num = buffer[counter]*2;
        file = fopen("file.txt", "a");
        fprintf(file,"\n%d\n" , num);
        fclose(file);
        sem_post(&semC);
        printf("Consumer Job Finished. \n");
        
    }
}

int main(void) {


    pthread_t tid0,tid1;
    sem_init(&semP, 0, 0);
    sem_init(&semC, 0, 0);

        pthread_create(&tid0, NULL, consumer, NULL);
        pthread_create(&tid1, NULL, producer, NULL);
        pthread_join(tid0, NULL);
        pthread_join(tid1, NULL);

    sem_destroy(&semC);
    sem_destroy(&semP);

    return 0;
}