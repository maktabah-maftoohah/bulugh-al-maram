"""Seed script for Bulugh al-Maram books and Book 1 data conforming to Maktabah Maftoohah standards."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BOOKS_FILE = DATA_DIR / "books.json"
CHAPTERS_DIR = DATA_DIR / "chapters"
HADITHS_DIR = DATA_DIR / "hadiths"

# Canonical 16 books of Bulugh al-Maram
BOOKS_DATA = [
  {"book_number": 1, "title_ar": "كتاب الطهارة", "title_ms": "Kitab Bersuci (Taharah)", "title_en": "Book of Purification", "hadith_start": 1, "hadith_end": 144, "hadith_count": 144},
  {"book_number": 2, "title_ar": "كتاب الصلاة", "title_ms": "Kitab Solat", "title_en": "Book of Prayer", "hadith_start": 145, "hadith_end": 533, "hadith_count": 389},
  {"book_number": 3, "title_ar": "كتاب الجنائز", "title_ms": "Kitab Jenazah", "title_en": "Book of Funerals", "hadith_start": 534, "hadith_end": 605, "hadith_count": 72},
  {"book_number": 4, "title_ar": "كتاب الزكاة", "title_ms": "Kitab Zakat", "title_en": "Book of Zakat", "hadith_start": 606, "hadith_end": 673, "hadith_count": 68},
  {"book_number": 5, "title_ar": "كتاب الصيام", "title_ms": "Kitab Puasa (Siyam)", "title_en": "Book of Fasting", "hadith_start": 674, "hadith_end": 716, "hadith_count": 43},
  {"book_number": 6, "title_ar": "كتاب الحج", "title_ms": "Kitab Haji", "title_en": "Book of Pilgrimage (Hajj)", "hadith_start": 717, "hadith_end": 794, "hadith_count": 78},
  {"book_number": 7, "title_ar": "كتاب البيوع", "title_ms": "Kitab Jual Beli (Muamalat)", "title_en": "Book of Business Transactions", "hadith_start": 795, "hadith_end": 966, "hadith_count": 172},
  {"book_number": 8, "title_ar": "كتاب النكاح", "title_ms": "Kitab Nikah (Munakahat)", "title_en": "Book of Marriage", "hadith_start": 967, "hadith_end": 1109, "hadith_count": 143},
  {"book_number": 9, "title_ar": "كتاب الجنايات", "title_ms": "Kitab Jenayah (Jinayat)", "title_en": "Book of Crimes & Retaliation", "hadith_start": 1110, "hadith_end": 1160, "hadith_count": 51},
  {"book_number": 10, "title_ar": "كتاب الحدود", "title_ms": "Kitab Hukuman Hudud", "title_en": "Book of Prescribed Punishments", "hadith_start": 1161, "hadith_end": 1228, "hadith_count": 68},
  {"book_number": 11, "title_ar": "كتاب الجهاد", "title_ms": "Kitab Jihad", "title_en": "Book of Jihad", "hadith_start": 1229, "hadith_end": 1297, "hadith_count": 69},
  {"book_number": 12, "title_ar": "كتاب الأطعمة", "title_ms": "Kitab Makanan dan Sembelihan", "title_en": "Book of Foods and Slaughtering", "hadith_start": 1298, "hadith_end": 1362, "hadith_count": 65},
  {"book_number": 13, "title_ar": "كتاب الأيمان والنذور", "title_ms": "Kitab Sumpah dan Nazar", "title_en": "Book of Oaths and Vows", "hadith_start": 1363, "hadith_end": 1386, "hadith_count": 24},
  {"book_number": 14, "title_ar": "كتاب القضاء", "title_ms": "Kitab Kehakiman dan Saksi", "title_en": "Book of Judgments and Witnesses", "hadith_start": 1387, "hadith_end": 1422, "hadith_count": 36},
  {"book_number": 15, "title_ar": "كتاب العتق", "title_ms": "Kitab Memerdekakan Hamba", "title_en": "Book of Emancipation of Slaves", "hadith_start": 1423, "hadith_end": 1445, "hadith_count": 23},
  {"book_number": 16, "title_ar": "كتاب الجامع", "title_ms": "Kitab al-Jami' (Adab, Zuhd & Akhlak)", "title_en": "The Comprehensive Book (Manners & Morals)", "hadith_start": 1446, "hadith_end": 1596, "hadith_count": 151}
]

# Book 1 Chapters
CHAPTERS_BOOK_1 = [
  {"chapter_number": 1, "title_ar": "باب الْمِيَاهِ", "title_ms": "Bab Air", "title_en": "Chapter on Waters", "hadith_start": 1, "hadith_end": 14},
  {"chapter_number": 2, "title_ar": "باب الآنِيَةِ", "title_ms": "Bab Bekas dan Bejana", "title_en": "Chapter on Utensils", "hadith_start": 15, "hadith_end": 23},
  {"chapter_number": 3, "title_ar": "باب إِزَالَةِ النَّجَاسَةِ وَبَيَانِهَا", "title_ms": "Bab Menghilangkan Najis", "title_en": "Chapter on Cleansing Impurities", "hadith_start": 24, "hadith_end": 35},
  {"chapter_number": 4, "title_ar": "باب الْوُضُوءِ", "title_ms": "Bab Wuduk", "title_en": "Chapter on Ablution (Wudu')", "hadith_start": 36, "hadith_end": 64}
]

# Book 1 Hadiths 1-5
HADITHS_BOOK_1 = [
  {
    "collection_id": "bulugh-al-maram",
    "hadith_number": 1,
    "in_book_number": 1,
    "book_number": 1,
    "book_title": {"ar": "كتاب الطهارة", "ms": "Kitab Bersuci (Taharah)", "en": "Book of Purification"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب الْمِيَاهِ", "ms": "Bab Air", "en": "Chapter on Waters"},
    "arabic": "عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ فِي الْبَحْرِ: «هُوَ الطَّهُورُ مَاؤُهُ، الْحِلُّ مَيْتَتُهُ».",
    "sanad_text": "عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ فِي الْبَحْرِ:",
    "matn_text": "«هُوَ الطَّهُورُ مَاؤُهُ، الْحِلُّ مَيْتَتُهُ».",
    "gradings": [{"scholar": "Al-Hafiz Ibn Hajar", "grade": "Sahih", "grade_ar": "صحيح", "notes": "أخرجه الأربعة وابن أبي شيبة واللفظ له، وصححه ابن خزيمة والترمذي"}],
    "translations": {
      "ms": "Daripada Abu Hurairah r.a. katanya: Rasulullah ﷺ bersabda mengenai air laut: 'Laut itu menyucikan airnya dan halal bangkainya.'",
      "en": "Narrated Abu Huraira: Allah's Messenger said regarding the sea: 'Its water is purifying and its dead (animals) are lawful to eat.'"
    },
    "tags": ["air-laut", "taharah", "makanan-laut", "hukum-bersuci"]
  },
  {
    "collection_id": "bulugh-al-maram",
    "hadith_number": 2,
    "in_book_number": 2,
    "book_number": 1,
    "book_title": {"ar": "كتاب الطهارة", "ms": "Kitab Bersuci (Taharah)", "en": "Book of Purification"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب الْمِيَاهِ", "ms": "Bab Air", "en": "Chapter on Waters"},
    "arabic": "وَعَنْ أَبِي سَعِيدٍ الْخُدْرِيِّ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «إِنَّ الْمَاءَ طَهُورٌ لا يُنَجِّسُهُ شَيْءٌ».",
    "sanad_text": "وَعَنْ أَبِي سَعِيدٍ الْخُدْرِيِّ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "«إِنَّ الْمَاءَ طَهُورٌ لا يُنَجِّسُهُ شَيْءٌ».",
    "gradings": [{"scholar": "Al-Hafiz Ibn Hajar", "grade": "Sahih", "grade_ar": "صحيح", "notes": "أخرجه الثلاثة وصححه أحمد"}],
    "translations": {
      "ms": "Daripada Abu Sa'id al-Khudri r.a. katanya: Rasulullah ﷺ bersabda: 'Sesungguhnya air itu suci lagi menyucikan, tidak ada sesuatu pun yang dapat menajiskannya.'",
      "en": "Narrated Abu Sa'id Al-Khudri: Allah's Messenger said: 'Water is pure and nothing can make it impure.'"
    },
    "tags": ["sifat-air", "kesucian-air", "taharah"]
  },
  {
    "collection_id": "bulugh-al-maram",
    "hadith_number": 3,
    "in_book_number": 3,
    "book_number": 1,
    "book_title": {"ar": "كتاب الطهارة", "ms": "Kitab Bersuci (Taharah)", "en": "Book of Purification"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب الْمِيَاهِ", "ms": "Bab Air", "en": "Chapter on Waters"},
    "arabic": "وَعَنْ عَبْدِ اللَّهِ بْنِ عُمَرَ رَضِيَ اللَّهُ عَنْهُمَا قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «إِذَا كَانَ الْمَاءُ قُلَّتَيْنِ لَمْ يَحْمِلِ الْخَبَثَ». وَفِي لَفْظٍ: «لَمْ يَنْجُسْ».",
    "sanad_text": "وَعَنْ عَبْدِ اللَّهِ بْنِ عُمَرَ رَضِيَ اللَّهُ عَنْهُمَا قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "«إِذَا كَانَ الْمَاءُ قُلَّتَيْنِ لَمْ يَحْمِلِ الْخَبَثَ». وَفِي لَفْظٍ: «لَمْ يَنْجُسْ».",
    "gradings": [{"scholar": "Al-Hafiz Ibn Hajar", "grade": "Sahih", "grade_ar": "صحيح", "notes": "أخرجه الأربعة وصححه ابن خزيمة وابن حبان"}],
    "translations": {
      "ms": "Daripada Abdullah ibn 'Umar r.a. katanya: Rasulullah ﷺ bersabda: 'Apabila air telah mencapai kadar dua qullah, ia tidak mengandungi najis.' Dan dalam suatu riwayat: 'Ia tidak menjadi najis.'",
      "en": "Narrated 'Abdullah bin 'Umar: Allah's Messenger said: 'When the water reaches the amount of two Qullahs (large jars), it does not carry impurity.' In another narration: 'It does not become impure.'"
    },
    "tags": ["kadar-dua-qullah", "hukum-air-banyak", "fiqh-taharah"]
  },
  {
    "collection_id": "bulugh-al-maram",
    "hadith_number": 4,
    "in_book_number": 4,
    "book_number": 1,
    "book_title": {"ar": "كتاب الطهارة", "ms": "Kitab Bersuci (Taharah)", "en": "Book of Purification"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب الْمِيَاهِ", "ms": "Bab Air", "en": "Chapter on Waters"},
    "arabic": "وَعَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «لا يَغْتَسِلْ أَحَدُكُمْ فِي الْمَاءِ الدَّائِمِ وَهُوَ جُنُبٌ».",
    "sanad_text": "وَعَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "«لا يَغْتَسِلْ أَحَدُكُمْ فِي الْمَاءِ الدَّائِمِ وَهُوَ جُنُبٌ».",
    "gradings": [{"scholar": "Al-Hafiz Ibn Hajar", "grade": "Sahih", "grade_ar": "صحيح", "notes": "أخرجه مسلم، وللبخاري: «لا يَبُولَنَّ أَحَدُكُمْ فِي الْمَاءِ الدَّائِمِ الَّذِي لا يَجْرِي ثُمَّ يَغْتَسِلُ فِيهِ»"}],
    "translations": {
      "ms": "Daripada Abu Hurairah r.a. katanya: Rasulullah ﷺ bersabda: 'Janganlah seseorang daripada kamu mandi di dalam air yang tenang (tidak mengalir) sedang dia dalam keadaan berjunub.'",
      "en": "Narrated Abu Huraira: Allah's Messenger said: 'None of you should take a bath in stagnant water when he is sexually defiled (in a state of Janaba).'"
    },
    "tags": ["air-tenang", "mandi-janabah", "adab-kebersihan"]
  },
  {
    "collection_id": "bulugh-al-maram",
    "hadith_number": 5,
    "in_book_number": 5,
    "book_number": 1,
    "book_title": {"ar": "كتاب الطهارة", "ms": "Kitab Bersuci (Taharah)", "en": "Book of Purification"},
    "chapter_number": 2,
    "chapter_title": {"ar": "باب الآنِيَةِ", "ms": "Bab Bekas dan Bejana", "en": "Chapter on Utensils"},
    "arabic": "وَعَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «طَهُورُ إِنَاءِ أَحَدِكُمْ إِذَا وَلَغَ فِيهِ الْكَلْبُ أَنْ يَغْسِلَهُ سَبْعَ مَرَّاتٍ، أُولاهُنَّ بِالتُّرَابِ».",
    "sanad_text": "وَعَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "«طَهُورُ إِنَاءِ أَحَدِكُمْ إِذَا وَلَغَ فِيهِ الْكَلْبُ أَنْ يَغْسِلَهُ سَبْعَ مَرَّاتٍ، أُولاهُنَّ بِالتُّرَابِ».",
    "gradings": [{"scholar": "Al-Hafiz Ibn Hajar", "grade": "Sahih", "grade_ar": "صحيح", "notes": "أخرجه مسلم"}],
    "translations": {
      "ms": "Daripada Abu Hurairah r.a. katanya: Rasulullah ﷺ bersabda: 'Menyucikan bekas seseorang daripada kamu apabila dijilat anjing adalah dengan membasuhnya sebanyak tujuh kali, yang pertamanya dengan tanah.'",
      "en": "Narrated Abu Huraira: Allah's Messenger said: 'The cleansing of the utensil of one of you when a dog has licked it is to wash it seven times, the first with dust.'"
    },
    "tags": ["jilatan-anjing", "samak-najis-mughallazah", "bekas-makanan"]
  }
]

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    HADITHS_DIR.mkdir(parents=True, exist_ok=True)

    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(BOOKS_DATA, f, ensure_ascii=False, indent=2)
    print(f"Written {len(BOOKS_DATA)} books to {BOOKS_FILE}")

    chap_file = CHAPTERS_DIR / "01.json"
    with open(chap_file, "w", encoding="utf-8") as f:
        json.dump(CHAPTERS_BOOK_1, f, ensure_ascii=False, indent=2)
    print(f"Written {len(CHAPTERS_BOOK_1)} chapters to {chap_file}")

    hadith_file = HADITHS_DIR / "01.json"
    with open(hadith_file, "w", encoding="utf-8") as f:
        json.dump(HADITHS_BOOK_1, f, ensure_ascii=False, indent=2)
    print(f"Written {len(HADITHS_BOOK_1)} hadiths to {hadith_file}")

    coll_file = DATA_DIR / "collection.json"
    coll_data = {
      "collection": "bulugh-al-maram",
      "title": "Maktabah Maftoohah — Bulugh al-Maram",
      "title_ar": "بلوغ المرام من أدلة الأحكام",
      "total_books": len(BOOKS_DATA),
      "total_hadiths": 1596,
      "seeded_books": [1],
      "active_hadiths": len(HADITHS_BOOK_1)
    }
    with open(coll_file, "w", encoding="utf-8") as f:
        json.dump(coll_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {coll_file}")

if __name__ == "__main__":
    main()
