#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES INTRC_IO                 //High speed Osc (> 4mhz for PCM/PCH) (>10mhz for PCD)
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOPROTECT                //Code not protected from reading
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOMCLR                   //No Master Clear pin enabled
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection



#define CHIFFRE_0 0x40 // 0x3F
#define CHIFFRE_1 0x79 // 0x06
#define CHIFFRE_2 0x24 // 0x5B
#define CHIFFRE_3 0x30 // 0x4F
#define CHIFFRE_4 0x19 // 0x66
#define CHIFFRE_5 0x12 // 0x6D
#define CHIFFRE_6 0x02 // 0x7D
#define CHIFFRE_7 0x58 // 0x27
#define CHIFFRE_8 0x00 // 0x7F
#define CHIFFRE_9 0x10 // 0x6F

#define CHIFFRE_A 0x20 // 0x5F
#define CHIFFRE_B 0x03 // 0x7C
#define CHIFFRE_C 0x27 // 0x58
#define CHIFFRE_D 0x21 // 0x5E
#define CHIFFRE_E 0x04 // 0x7B
#define CHIFFRE_F 0x0E // 0x71
#define CHIFFRE_G 0x10 // 0x6F
#define CHIFFRE_H 0x09 // 0x76
#define CHIFFRE_I 0x4F // 0x30
#define CHIFFRE_J 0x61 // 0x1E
#define CHIFFRE_K 0x09 // 0x76
#define CHIFFRE_L 0x43 // 0x3C
#define CHIFFRE_M 0x48 // 0x37
#define CHIFFRE_N 0x2B // 0x54
#define CHIFFRE_O 0x23 // 0x5C
#define CHIFFRE_P 0x0C // 0x73
#define CHIFFRE_Q 0x18 // 0x67
#define CHIFFRE_R 0x2F // 0x50
#define CHIFFRE_S 0x12 // 0x6D
#define CHIFFRE_T 0x07 // 0x78
#define CHIFFRE_U 0x63 // 0x1C
#define CHIFFRE_V 0x63 // 0x1C
#define CHIFFRE_W 0x63 // 0x1C
#define CHIFFRE_X 0x09 // 0x76
#define CHIFFRE_Y 0x11 // 0x6E
#define CHIFFRE_Z 0x24 // 0x5B

#define CHIFFRE_TIRET  0x3F // 0x40
#define CHIFFRE_ESPACE 0x7F // 0x00
#define CHIFFRE_OFF    0x7F // 0x00

#define BLTM        244 //488 = 1s

#define DATA_PIN  PIN_A0
#define CLK_PIN   PIN_A2
#define STB_PIN   PIN_A1

#define RQ_SD_DT  PIN_B0
#define RX        PIN_B1
#define SD_OK     PIN_B3

#define DIG_0     PIN_B7
#define DIG_1     PIN_B6
#define DIG_2     PIN_B5

#define DIG_EN    PIN_B4

#define CHIFF_COUNT  4

#use delay(clock=4000000)
#use rs232(baud=9600,parity=N,xmit=PIN_B2,rcv=RX,bits=8)

