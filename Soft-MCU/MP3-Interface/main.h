#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES HS                       //High speed Osc (> 4mhz for PCM/PCH) (>10mhz for PCD)
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOPROTECT                //Code not protected from reading
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOMCLR                   //Master Clear pin used for I/O
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection


#define MP3_TX                PIN_A2
#define MP3_RQ_SD             PIN_A3

#define OUTPUT_ENABLE         PIN_B3
#define PIC_RX                PIN_B1
#define PIC_TX                PIN_B2

#define MP3_READY             PIN_B7
#define MP3_ON_OFF            PIN_B4
#define MP3_CMD_OUT           PIN_B5

#use delay(clock=8000000)
#use rs232(baud=19200,parity=N,rcv=MP3_TX,bits=8,stream=in)
#use rs232(baud=19200,parity=N,xmit=PIC_TX,rcv=PIC_RX,bits=8,stream=out)

