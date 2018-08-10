#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES INTRC_IO                 //Internal RC Osc, no CLKOUT
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOPROTECT                //Code not protected from reading
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOMCLR                   //Master Clear pin used for I/O
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection

#define CLK_PIN      PIN_A6
#define PS_PIN       PIN_B7

#define MP3_RQ_SEND  PIN_B0
#define MP3_TX       PIN_B2
#define MP3_READY    PIN_B3

#define DO11_PIN     PIN_A0
#define DO12_PIN     PIN_A7
#define DO13_PIN     PIN_A1

#define DO21_PIN     PIN_B5
#define DO22_PIN     PIN_B4
#define DO23_PIN     PIN_B6

#use delay(clock=4000000)
#use rs232(baud=19200,parity=N,xmit=MP3_TX,rcv=PIN_B1,bits=8)

