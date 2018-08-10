#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOPUT                    //No Power Up Timer
#FUSES INTRC_IO                 //Internal RC Osc, no CLKOUT
#FUSES NOMCLR                   //Master Clear pin used for I/O
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection
#FUSES NOPROTECT                //Code not protected from reading

#define IR_SIGNAL       PIN_A6

#define IR_RQ_SEND      PIN_B0
#define IR_DATA_READY   PIN_B3

#use delay(clock=4000000)
#use rs232(baud=9600,xmit=PIN_B2,rcv=PIN_B1,bits=8)

