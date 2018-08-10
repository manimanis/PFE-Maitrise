#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES HS                       //High speed Osc (> 4mhz for PCM/PCH) (>10mhz for PCD)
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOPROTECT                //Code not protected from reading
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOMCLR                   //Master Clear pin used for I/O
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection

#define LCD_RW       PIN_A0
#define LCD_RS       PIN_A1
#define LCD_E        PIN_A2
#define LCD_BKL      PIN_B4

#define SH_DATA      PIN_A3
#define SH_STB       PIN_B0
#define SH_CLK       PIN_B3

#define ENABLE_INT   enable_interrupts(GLOBAL)
#define DISABLE_INT  disable_interrupts(GLOBAL)

#use delay(clock=20000000)
#use rs232(baud=9600,parity=N,xmit=PIN_B2,rcv=PIN_B1,bits=8)

