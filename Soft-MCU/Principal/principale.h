#include <18F4550.h>
#device adc=8

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES WDT128                   //Watch Dog Timer uses 1:128 Postscale
#FUSES PLL5                     //Divide By 5(20MHz oscillator input)
#FUSES CPUDIV2                  //System Clock by 2
#FUSES USBDIV                   //USB clock source comes from primary oscillator
#FUSES HSPLL                    //High Speed Crystal/Resonator with PLL enabled
#FUSES FCMEN                    //Fail-safe clock monitor enabled
#FUSES IESO                     //Internal External Switch Over mode enabled
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES BORV20                   //Brownout reset at 2.0V
#FUSES VREGEN                   //USB voltage regulator enabled
#FUSES PBADEN                   //PORTB pins are configured as analog input channels on RESET
#FUSES LPT1OSC                  //Timer1 configured for low-power operation
#FUSES NOMCLR                   //Master Clear pin disabled
#FUSES STVREN                   //Stack full/underflow will cause reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOXINST                  //Extended set extension and Indexed Addressing mode disabled (Legacy mode)
#FUSES NODEBUG                  //No Debug mode for ICD
#FUSES NOPROTECT                //Code not protected from reading
#FUSES NOCPB                    //No Boot Block code protection
#FUSES NOCPD                    //No EE protection
#FUSES NOWRT                    //Program memory not write protected
#FUSES NOWRTC                   //configuration not registers write protected
#FUSES NOWRTB                   //Boot block not write protected
#FUSES NOWRTD                   //Data EEPROM not write protected
#FUSES NOEBTR                   //Memory not protected from table reads
#FUSES NOEBTRB                  //Boot block not protected from table reads

#define AFF_TX             PIN_A0
#define AFF2               PIN_A1
#define AFF1               PIN_A2
#define AFF0               PIN_A3

#define LDARR1_DATA        PIN_D1
#define LDARR2_DATA        PIN_A5

#define LCD_DATA           PIN_D2

#define IR_DATA_READY      PIN_D4
#define IR_RX              PIN_D5
#define IR_RQ_SEND         PIN_D6

#define DISABLE_INT        disable_interrupts(GLOBAL)
#define ENABLE_INT         enable_interrupts(GLOBAL)

#use delay(crystal=20000000,  clock=48000000)
#use i2c(master,sda=PIN_B0,scl=PIN_B1)
#use rs232(baud=9600,rcv=PIN_C7,xmit=PIN_C6,bits=8)
#use rs232(baud=9600,xmit=AFF_TX,bits=8,stream=aff7)
#use rs232(baud=9600,xmit=LDARR1_DATA,bits=8,stream=ld1)
#use rs232(baud=9600,xmit=LDARR2_DATA,bits=8,stream=ld2)
#use rs232(baud=9600,xmit=LCD_DATA,bits=8,stream=lcd)
#use rs232(baud=9600,rcv=IR_RX,bits=8,stream=ir)
#use rs232(baud=19200,rcv=PIN_C0,xmit=PIN_C2,bits=8,stream=mp3)

