#include <main.h>

BYTE CONST rmt_data [66] = {
   0xff, 0xaa, 0xaa, // 0 - Preambule   
   0xb7, 0xbb, 0x56, // 1 - ON/OFF
   0xd7, 0xb7, 0x56, // 2 - Mode
   0xab, 0xdf, 0x56, // 3 - Mute
   0xef, 0x6b, 0x56, // 4 - Prev
   0xfe, 0xd5, 0x56, // 5 - Next
   0xaf, 0xbd, 0x56, // 6 - Play/Pause
   0xab, 0xfe, 0xaa, // 7 - Vol-
   0xb6, 0xfb, 0x6a, // 8 - Vol+
   0xbb, 0xf5, 0xaa, // 9 - EQ
   0xd6, 0xf7, 0x6a, // 10 - 0
   0xba, 0xfa, 0xea, // 11 - 100+
   0xb5, 0xfb, 0xaa, // 12 - Replay
   0xeb, 0xeb, 0xaa, // 13 - 1
   0xf5, 0xea, 0xea, // 14 - 2
   0xd5, 0x6d, 0xf6, // 15 - 3
   0xf7, 0xd5, 0xaa, // 16 - 4
   0xea, 0xf5, 0xea, // 17 - 5
   0xda, 0xdb, 0x76, // 18 - 6
   0xdf, 0x6d, 0x56, // 19 - 7
   0xdd, 0xb6, 0xb6, // 20 - 8
   0xdb, 0xb6, 0xd6  // 21 - 9
   };

#define RMTCTRL_ON_OFF        1     //A
#define RMTCTRL_MODE          2     //B
#define RMTCTRL_MUTE          3     //C
#define RMTCTRL_PREV          4     //D
#define RMTCTRL_NEXT          5     //E
#define RMTCTRL_PAUSE         6     //F
#define RMTCTRL_DEC_VOL       7     //G
#define RMTCTRL_INC_VOL       8     //H
#define RMTCTRL_EQ            9     //I
#define RMTCTRL_DIG_0         10    //J
#define RMTCTRL_DIG_100       11    //K
#define RMTCTRL_REPLAY        12    //L
#define RMTCTRL_DIG_1         13    //M
#define RMTCTRL_DIG_2         14    //N
#define RMTCTRL_DIG_3         15    //O
#define RMTCTRL_DIG_4         16    //P
#define RMTCTRL_DIG_5         17    //Q
#define RMTCTRL_DIG_6         18    //R
#define RMTCTRL_DIG_7         19    //S
#define RMTCTRL_DIG_8         20    //T
#define RMTCTRL_DIG_9         21    //U


#define STATE_PLAYING_START      1
#define STATE_PLAYING_TRACK      2
#define STATE_PAUSE              3
#define STATE_VOLUME             4
#define STATE_OTHER              0

char state[5];
char curr_pos[4];
int is_playing;
int curr_state, old_state;
int16 st, ost;
int* pst;
int etat;

void rmt_ctrl_byte(int data) {
   int1 bt;
   signed int i;
   for (i = 7 ; i >= 0 ; i--) {
      bt = bit_test(data, i);
      if (bt) {
         output_low(MP3_CMD_OUT);
         delay_us(533);
         
         output_high(MP3_CMD_OUT);
         delay_us(560);
      } else {
         output_high(MP3_CMD_OUT);
         delay_us(1093);
      }
   }
}

void rmt_ctrl_cmd(int cmd) {
   int pos;
   int v;
   
   disable_interrupts(GLOBAL);
   pos = cmd * 3;
  
   // Start Sequence
   output_low(MP3_CMD_OUT);
   delay_us(8885);
   
   output_high(MP3_CMD_OUT);
   delay_us(4456);
  
   // Préambule
   v = rmt_data[0];
   rmt_ctrl_byte(v);
   v = rmt_data[1];
   rmt_ctrl_byte(v);
   v = rmt_data[2];
   rmt_ctrl_byte(v);
   
   // Commande
   v = rmt_data[pos];
   rmt_ctrl_byte(v);
   v = rmt_data[pos+1];
   rmt_ctrl_byte(v);
   v = rmt_data[pos+2];
   rmt_ctrl_byte(v);
   
   // Stop Sequence
   // Un Logique
   output_low(MP3_CMD_OUT);
   delay_us(533);
   
   output_high(MP3_CMD_OUT);
   delay_us(560);
   
   output_high(MP3_CMD_OUT);
   delay_us(39466);
   
   output_low(MP3_CMD_OUT);
   delay_us(8877);
   
   output_high(MP3_CMD_OUT);
   delay_us(2250);
   
   output_low(MP3_CMD_OUT);
   delay_us(533);
   
   output_high(MP3_CMD_OUT);
   delay_us(560);
   
   output_high(MP3_CMD_OUT);
   delay_ms(95);
   
   output_low(MP3_CMD_OUT);
   delay_us(8877);
   
   output_high(MP3_CMD_OUT);
   delay_us(2250);
   
   output_low(MP3_CMD_OUT);
   delay_us(533);
   
   output_high(MP3_CMD_OUT);
   delay_us(560);
   // 226.90ms
   
   delay_ms(273);
   enable_interrupts(GLOBAL);
}

void disable_sounds() {
   is_playing = FALSE; 
   output_low(MP3_ON_OFF);
}

void enable_sounds() {
   is_playing = TRUE; 
   st = 0;
   etat = 0;
   output_high(MP3_ON_OFF);
}

#INT_RDA
void rda_isr() {
   char c;
   c = fgetc(out);
   if (c == 'P') {
      enable_sounds();
   } else if (c == 'S') {
      disable_sounds();
   } else if (c == 'Y') {
      fputc(is_playing, out);
      fputc(*pst, out);
      fputc(*(pst+1), out);
   }
}

int16 calc_value() {
   return ((state[1] - '0') * 600) + 
          ((state[2] - '0') * 60) + 
          ((state[3] - '0') * 10) + 
          (state[4] - '0');
}

void main()
{  
   int c;
   enable_interrupts(INT_RDA);
   enable_interrupts(GLOBAL);
   
   output_high(MP3_CMD_OUT);
   delay_ms(1000);
   
   disable_sounds();
   
   pst = &ost;
   ost = 12350;
   
   while (TRUE) {
      do {
         c = fgetc(in);
      } while (c != '!');
      
      state[0] = fgetc(in);
      state[1] = fgetc(in);
      state[2] = fgetc(in);
      state[3] = fgetc(in);
      state[4] = fgetc(in);
      
      curr_state = state[0];
      ost = calc_value();
      if (curr_state == 0x7b && old_state == 0x6b) {
         disable_sounds();
      }
      old_state = curr_state;
   }
}

/*
Etat              Affichage
PAUSE             USB+" PAU"
X                 USB+"000X" (X dans [1..9])
Lecture           USB:+"XXXX" (X position)
*/
