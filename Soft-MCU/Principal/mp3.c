#include "mp3.h"

int is_playing = 0, 
    curr_state = 0;
int16 mp3_pos = 0;

void play_mp3() {
   DISABLE_INT;
   fputc('P', mp3);
   is_playing = TRUE;
   ENABLE_INT;
}

void stop_mp3(){
   DISABLE_INT;
   fputc('S', mp3);
   is_playing = FALSE;
   ENABLE_INT;
}

void state_mp3() {
   int *p;
   p = &mp3_pos;
   DISABLE_INT;
   fputc('Y', mp3);
   curr_state = fgetc(mp3);
   p[0] = fgetc(mp3);
   p[1] = fgetc(mp3);
   ENABLE_INT;
}
