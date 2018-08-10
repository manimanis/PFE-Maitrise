#ifndef __AFF7SEG_H__

#define __AFF7SEG_H__

#define AFF7_DATE          7
#define AFF7_TIME          1
#define AFF7_FAJR          6
#define AFF7_CHOUROUK      4
#define AFF7_DHOHR         3
#define AFF7_ASR           5
#define AFF7_MAGHREB       2
#define AFF7_ISHAA         0

void aff7_select(int channel);
void aff7_show_time(int sel, int hh, int mm);
void aff7_show_date(int dd, int mm, int yy);
void aff7_show_time(int hh, int mm);
void aff7_show_prayers(int* prayers);

#endif // __AFF7SEG_H__
