#include "aff7seg.h"
#include "prieres.h"

int aff7_channel;
int aff7_state = TRUE;

void aff7_off() {
   putc('!', aff7);
   putc('$', aff7);
   putc(0x0F, aff7);   
}

void aff7_select(int channel) {
   aff7_channel = channel;
   
   output_bit(AFF0, bit_test(channel, 0));
   output_bit(AFF1, bit_test(channel, 1));
   output_bit(AFF2, bit_test(channel, 2));
   if (!aff7_state) {
      aff7_off();
   }
}

void aff7_show_time(int sel, int hh, int mm) {
   aff7_select(sel);
   if (!aff7_state) return;
   putc('!', aff7);
   putc((hh >> 4) + 0x30, aff7);
   putc((hh & 0x0f) + 0x30, aff7);
   putc((mm >> 4) + 0x30, aff7);
   putc((mm & 0x0f) + 0x30, aff7);
   putc('$', aff7);
   putc(0x0D, aff7);   
}

void aff7_show_prayers(int* prayers) {
   aff7_show_time(AFF7_FAJR, prayers[PRIERE_FAJR], prayers[PRIERE_FAJR + 1]);
   aff7_show_time(AFF7_CHOUROUK, prayers[PRIERE_CHOUROUK], prayers[PRIERE_CHOUROUK + 1]);
   aff7_show_time(AFF7_DHOHR, prayers[PRIERE_DHOHR], prayers[PRIERE_DHOHR + 1]);
   aff7_show_time(AFF7_ASR, prayers[PRIERE_ASR], prayers[PRIERE_ASR + 1]);
   aff7_show_time(AFF7_MAGHREB, prayers[PRIERE_MAGHREB], prayers[PRIERE_MAGHREB + 1]);
   aff7_show_time(AFF7_ISHAA, prayers[PRIERE_ISHAA], prayers[PRIERE_ISHAA + 1]);
}

void aff7_show_date(int dd, int mm, int yy) {
   aff7_select(AFF7_DATE);
   if (!aff7_state) return;
   putc('!', aff7);
   putc((dd >> 4) + 0x30, aff7);
   putc((dd & 0x0f) + 0x30, aff7);
   putc('-', aff7);
   putc((mm >> 4) + 0x30, aff7);
   putc((mm & 0x0f) + 0x30, aff7);
   putc('-', aff7);
   putc(0x32, aff7);
   putc(0x30, aff7);
   putc((yy >> 4) + 0x30, aff7);
   putc((yy & 0x0f) + 0x30, aff7);
   putc(' ', aff7);
   putc(' ', aff7);
   putc(' ', aff7);
   putc(' ', aff7);
   putc('$', aff7);
   putc(0x0f, aff7);
}

void aff7_show_time(int hh, int mm) {
   aff7_select(AFF7_TIME);
   if (!aff7_state) return;
   putc('!', aff7);
   putc((clk_data[2] >> 4) + 0x30, aff7);
   putc((clk_data[2] & 0x0f) + 0x30, aff7);
   putc((clk_data[1] >> 4) + 0x30, aff7);
   putc((clk_data[1] & 0x0f) + 0x30, aff7);
   putc('$', aff7);
}
