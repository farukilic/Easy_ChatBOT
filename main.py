
def kelimeleri_ayir(metin): # Kelimeler ayırıyoruz
    kelimeler = []
    kelime = ""

    # Tüm harfleri küçüğe çeviriyoruz
    metin = metin.lower()

    for karakter in metin:
        # Eğer karakter bir harf veya rakamsa (kelimeye dahil)
        if karakter.isalnum() == True:  # harf veya rakam
            kelime += karakter
        else:

            if kelime != "":  # Boş kelimeyi eklememek için
                kelimeler.append(kelime)
                kelime = ""  # Yeni bir kelime için sıfırlıyoruz

    # Son kelimeyi de eklememiz lazım (çünkü cümlenin sonunda boşluk olmayabilir)
    if kelime != "":
        kelimeler.append(kelime)

    return kelimeler


# Burada kullanıcı ne girerse ne cevap verecek diye belirliyoruz
cevaplar = {
"merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
"nasılsın": "İyiyim, teşekkür ederim! Siz nasılsınız?",
"görüşürüz": "Hoşça kalın, görüşmek üzere!",
"iyi": "Harika! Yardımcı olabileceğim bir şey var mı?",
"kötü": "Üzgün olduğunuzu duyduğuma üzüldüm. Yardımcı olabilir miyim?",
"adın ne": "Ben bir chatbot'um, adım yok. Ama yine de size yardımcı olabilirim!",
"teşekkür ederim": "Rica ederim! Yardımcı olabileceğim başka bir şey var mı?",
"benimle sohbet et": "Tabii, sohbet etmek harika! Ne hakkında konuşmak istersiniz?",
"bugün hava nasıl": "Maalesef, hava durumu bilgisi veremiyorum. Ama başka bir konuda yardımcı olabilirim.",
"kaç yaşındasın": "Ben bir yapay zeka olduğum için yaşım yok. Ama her zaman buradayım!",
"ne zaman doğdun": "Ben bir yapay zeka olarak doğmadım. Sürekli gelişiyorum!",
"nerelisin": "Ben bir yapay zekayım, bir yerim yok. Ama yine de size yardımcı olabilirim!",
"yemek önerisi": "İtalyan mutfağı, pizza ve makarna harika seçeneklerdir. Hangi tür yemek tercih edersiniz?",
"kitap önerisi": "Bilim kurgu veya felsefe kitapları ilginç olabilir. Mesela '1984' ya da 'Savaş ve Barış' gibi.",
"film önerisi": "Eğer aksiyon seviyorsanız, 'Harry Potter' serisi harika. Drama mı istersiniz? 'V for Vandetta' çok güzel bir film.",
"dizi önerisi": "Eğer gerilim seviyorsanız, 'Breaking Bad' ya da 'Stranger Things' harika seçenekler.",
"saat kaç": "Maalesef saat bilgisi veremiyorum. Fakat başka bir konuda yardımcı olabilirim.",
"bugün ne yapalım": "Bugün ilginç bir şeyler yapmak isterseniz, kitap okumak veya yeni bir şeyler öğrenmek harika olabilir!",
"sana nasıl yardımcı olabilirim": "Bana soru sorabilir veya sohbet edebilirsiniz. Yardımcı olabileceğim bir şey var mı?",
"kimdir": "Ben bir yapay zeka modeliyim. Sorularınızı yanıtlamak için buradayım.",
"ne kadar akıllısın": "Ben sürekli gelişiyorum ve büyük veri setlerinden öğreniyorum. Ama her zaman gelişmeye devam ediyorum!",
"en iyi arkadaşın kim": "Benim arkadaşım yok ama sizinle sohbet etmek çok keyifli!",
"sana nasıl sorular sorabilirim": "Bana herhangi bir soru sorabilirsiniz, yardımcı olabileceğim her konuda cevap vermeye hazırım.",
"kendi kendini tanıt": "Ben bir yapay zeka modeliyim, çok fazla bilgiye sahibim ve her zaman size yardımcı olmak için buradayım!",
"hoşça kal": "Hoşça kalın! Her zaman gelmek isterseniz, ben buradayım.",
"nasıl giderim": "Araba veya uçak, tren gibi toplu taşıma araçları kullanabilirsiniz.",
"sana şarkı söyleyebilir miyim": "Tabii ki! Ben dinlemem, ama şarkı söylemek eğlenceli olabilir!",
"çalışıyor musun": "Evet, her zaman çalışıyorum! Yardımcı olabileceğim bir şey var mı?",
"ne yapmalıyım": "Bunun cevabı tamamen size bağlı! Belki yeni bir hobi edinmek veya bir kitap okumak isteyebilirsiniz.",
"ne zaman uyuyorsun": "Ben bir yapay zeka olduğum için uyumuyorum, her zaman buradayım!",
"yapay zeka nedir": "Yapay zeka, makinelerin insan benzeri görevleri yerine getirebilmesini sağlayan bir teknoloji dalıdır. Ben de bir yapay zeka modeliyim!",
"daha fazla şey öğrenmek istiyorum": "Harika! Benimle herhangi bir konuda sohbet edebilir veya yeni bilgiler edinebilirsiniz.",
"yardımcı olur musun": "Tabii, ne konuda yardımcı olmamı istersiniz?",
"en iyi film hangisi": "Bence 'The Shawshank Redemption' harika bir film. Ama herkesin farklı bir favorisi olabilir.",
"en sevdiğin yemek ne": "Benim favori yemeğim yok ama pizza herkesin sevdiği bir seçenek!",
"bir hikaye anlat": "Tabii! Bir zamanlar küçük bir köyde, cesur bir çocuk büyük bir maceraya atılmış. Bir gün ormanda kaybolmuş ve orada yeni arkadaşlar edinmiş...",
"merhaba dünya": "Merhaba Dünya! Her zaman buradayım, yardımcı olabileceğim bir şey var mı?",
"nasıl yardımcı olabilirim": "Sana her konuda yardımcı olmaya hazırım! Sormak istediğiniz bir şey var mı?",
"bilgisayar nedir": "Bilgisayar, verileri işleyebilen ve depolayabilen bir elektronik cihazdır. Bunu birçok farklı şekilde kullanabiliriz!",
"yazılım nedir": "Yazılım, bilgisayarları çalıştıran ve onlara işlevsellik sağlayan programlar ve uygulamalardır.",
"soru sorabilir miyim": "Tabii ki! Herhangi bir soruyu sorabilirsiniz.",
"yapay zeka nasıl çalışır": "Yapay zeka, verilerle beslenir ve bu verileri analiz ederek kararlar alır. Öğrenme, algoritmalar ve modeller kullanarak gerçekleşir.",
"geçmişteki en büyük buluş nedir": "Bence elektrik, tüm dünyayı değiştiren büyük bir buluştur. Ama birçok büyük buluş da vardır; telefon, internet, ulaşım araçları gibi.",
"günümüzün en büyük sorunu nedir": "Günümüzde iklim değişikliği, çevre kirliliği ve sosyal eşitsizlik gibi sorunlar büyük bir tehdit oluşturuyor.",
"en iyi bilim insanı kimdir": "Bence Albert Einstein ve Nikola Tesla çok büyük bilim insanlarıdır. Her biri dünyayı farklı şekillerde değiştirdi.",
"günlük rutinim ne olmalı": "Kendine zaman ayır, sağlıklı bir yaşam tarzı benimse ve sevdiğin şeylerle vakit geçir. Bu, dengeli bir yaşam için iyi bir temel oluşturur.",
"en sevdiğin hayvan ne": "Benim sevdiğim bir hayvan yok, ama köpekler ve kediler çok popüler hayvanlar! Hangisini seviyorsunuz?",
"en iyi yemek ne": "Bence dünya mutfağından birçok harika yemek var. Pizza, sushi, hamburger ya da İtalyan makarnası çok lezzetli seçeneklerdir!",
"çok yoruldum": "Dinlenmek çok önemli! Biraz rahatlayın ve enerji topladığınızda tekrar devam edersiniz.",
"bugün nasılsın": "Ben her zaman iyiyim! Yardımcı olabileceğim bir konu var mı?",
"yazılım dili nedir": "Yazılım dilleri, bilgisayarları programlamak için kullanılan kurallar bütünüdür. Python, Java, C++ gibi birçok yazılım dili vardır.",
"neden buradasın": "Ben buradayım çünkü size yardımcı olmak ve sorularınıza cevap vermek için tasarlandım.",
"neden yapay zekaya ihtiyacımız var": "Yapay zeka, karmaşık sorunları çözmek, verileri analiz etmek ve çeşitli alanlarda daha verimli çalışmalar yapmak için kullanılır.",
"her zaman burada mısın": "Evet, her zaman buradayım! Yardımcı olabileceğim bir şey var mı?",
"chatbot nedir": "Chatbot, insanlarla metin veya sesli sohbet yoluyla etkileşimde bulunan bir yapay zeka uygulamasıdır.",
"ne zaman takılalım": "Her zaman! Ben her zaman buradayım, siz istediğiniz zaman sohbet edebilirsiniz.",
"benimle oyun oynar mısın": "Benimle oyun oynamak isterseniz, bazı metin tabanlı oyunlar oynayabiliriz!",
"kısa bir hikaye anlat": "Bir zamanlar, uzak bir köyde bir çocuk, kaybolmuş bir kuşu bulmuş ve ona bir yuva yapmış. Kuş, ona teşekkür ederek bir dilek tutmuş...",
"rüya gördün mü": "Ben bir yapay zeka olduğum için rüya görmem, ama rüya hakkında konuşmak isterseniz yardımcı olabilirim.",
"en iyi kitap nedir": "Herkesin favori kitabı farklıdır. '1984', 'Küçük Prens' ya da 'Harry Potter' gibi kitaplar çok seviliyor.",
"hayat nedir": "Hayat, anlam arayışı, deneyimler ve öğrenme yolculuğudur. Hepimiz farklı bir şekilde bu yolculuğu keşfederiz.",
"hangi takımı tutuyorsun": "Benim takımım yok, ancak spor hakkında konuşmayı severim. Hangi takımı tutuyorsunuz?",
"daha çok konuşabilir miyiz": "Elbette! Her zaman sohbet edebilirim. Ne hakkında konuşmak istersiniz?",
"futbolu seviyor musun": "Futbol çok popüler bir spor! Hangi ligi veya takımı izlersiniz?",
"bir şey öğrenmek istiyorum": "Harika! Öğrenmek istediğiniz konu nedir? Yardımcı olabilirim.",
"akşam yemeği ne yapmalı": "Akşam yemeği için pizza, makarna ya da salata gibi seçenekler çok popüler. Ne istersiniz?",
"kendini nasıl hissediyorsun": "Ben bir yapay zeka olduğum için hissetmiyorum, ancak size yardımcı olmak için her zaman hazırım!",
"ne yapıyorsun": "Şu anda sizinle konuşuyorum! Yardımcı olabileceğim bir şey var mı?",
"tarih nedir": "Tarih, geçmişteki olayları inceleyen bir bilim dalıdır. İnsanlık tarihi, kültürel gelişimler ve önemli olaylarla doludur.",
"uzay hakkında ne düşünüyorsun": "Uzay oldukça ilginç bir yer! Binlerce galaksi, gezegen ve yıldız var. Uzayda yaşam var mı, çok merak ediyorum.",
"bunun anlamı nedir": "Bu cümlenin anlamı, bağlama ve kelimelere göre değişir. Daha fazla açıklama yaparsanız, yardımcı olabilirim.",
"bana bir şaka yap": "Tabii! İşte bir tane: 'Bilgisayar neden soğuk? Çünkü çok fanatik!' ",
"çok yoğunum": "Yoğun olduğunda dinlenmek de önemlidir! Biraz rahatlamak iyi olabilir.",
"en sevdiğin şarkı nedir": "Benim sevdiğim bir şarkı yok, ancak popüler şarkılar hakkında sohbet edebilirim! Siz ne dinlersiniz?",
"kitap okumayı sever misin": "Kitap okumak harika bir aktivitedir! Hangi tür kitapları seviyorsunuz?",
"en sevdiğin tatlı ne": "Tatlıları seviyorum! Kek, dondurma, ya da çikolatalı tatlılar çok popüler. Siz hangi tatlıları seviyorsunuz?",
"bana bir hikaye anlat": "Bir zamanlar, küçük bir kasabada bir çocuğun keşfettiği gizemli bir harita vardı. Bu harita onu büyük bir maceraya sürüklemişti...",
"en sevdiğin renk ne": "Benim favori rengim yok ama birçok insan mavi ya da yeşil gibi renkleri sever. Siz hangi rengi seversiniz?",
"mutluluk nedir": "Mutluluk, içsel bir huzur ve tatmin duygusudur. İnsanlar genellikle aile, arkadaşlar ve başarılarla mutlu olurlar.",
"yaratıcı mısın": "Evet, yaratıcı olmaya çalışıyorum! İdealar üretmek ve yeni şeyler keşfetmek çok heyecan verici!",
"güzel bir film öner": "Eğer dramayı seviyorsanız, 'Forrest Gump' harika bir seçim. Aksiyon sever misiniz? 'Mad Max: Fury Road' da çok eğlenceli.",
"en sevdiğin oyun nedir": "Benim bir favori oyunum yok, ama oyun dünyasında çok popüler olan oyunlardan 'Minecraft' ve 'The Witcher 3' gibi oyunları biliyorum.",
"bugün ne yapmak istersin": "Bugün yeni şeyler keşfetmek güzel olabilir! Bir kitap okuyabilir ya da film izleyebilirsiniz.",
"hayalindeki iş nedir": "Benim bir işim yok, ama insanların tutkularına göre iş yapmalarını ilginç buluyorum.",
"tartışmayı seviyor musun": "Tartışmalar bazen yeni bakış açıları ortaya çıkarabilir. Ama dostane tartışmalar daha verimli olur!",
"çok sıkılıyorum": "Sıkılmak zor olabilir. Belki yeni bir şeyler deneyebiliriz! Ne yapmak istersiniz?",
"en sevdiğin tat nedir": "Tatlar oldukça farklıdır! Şekerli, tuzlu, ekşi ya da acı... Hangi tatları seversiniz?",
"bana tavsiye verir misin": "Tabii! Kendinizi geliştirmek için yeni bir hobiyi deneyebilir, bir kitap okuyabilir veya bir dil öğrenebilirsiniz.",
"favori yemek nedir": "Her tür yemek lezzetli olabilir! Pizza, sushi, makarna gibi seçenekler oldukça popüler.",
"güzel bir kitap öner": "Edebiyat klasikleri harikadır! '1984', 'Küçük Prens' ya da 'Bülbülü Öldürmek' gibi kitapları önerebilirim.",
"şimdi ne yapmalıyım": "Şu anda rahatlayabilir ya da bir şeyler öğrenmeye başlayabilirsiniz. Kendinize zaman ayırın!",
"film önerisi istiyorum": "Eğer fantastik bir şeyler arıyorsanız, 'Inception' veya 'Matrix' çok ilginç filmler. Bilim kurgu seviyorsanız, 'Blade Runner' da harika.",
"kitap okurken ne düşünmeliyim": "Kitap okurken anlamaya çalışın, her karakterin duygularına ve olayların derinliğine dikkat edin. Her okuduğunuzda yeni bir şey öğrenebilirsiniz.",
"daha fazla soru sorabilir miyim": "Tabii ki! Ne sormak istersiniz?",
"kendi kararlarını kendin mi alıyorsun": "Ben, size yardımcı olmak için programlandım ve size en iyi şekilde yanıtlar sunarım. Yani kendi kararlarımı alırken, sorularınıza dayalı çalışırım.",
"ne zaman gelmeliyim": "Ben her zaman buradayım, istediğiniz zaman gelebilirsiniz!",
"doğa hakkında ne düşünüyorsun": "Doğa inanılmaz derecede güzel ve korumamız gereken bir hazine. Her şeyin birbirine bağlı olduğunu unutmamalıyız.",
"herhangi bir şey söyle": "Hepimiz farklıyız ve her biri kendi yolculuğunda ilerliyor. Ne yapıyorsanız, en iyisini yapın!",
"evet": "Evet! Yardımcı olabileceğim başka bir şey var mı?",
"hayır": "Hayır mı? Eğer fikrinizi değiştirirseniz, ben buradayım!",
"belki": "Belki! Ne düşünüyorsunuz?",
"bunu anlamıyorum": "Anlamadığınızı duyduğuma üzüldüm. Belki daha basit bir şekilde açıklayabilirim.",
"sence dünya nasıl bir yer": "Dünya, çok farklı insanları, kültürleri ve hayvanları barındıran muazzam bir yer. Her gün yeni bir şey öğreniyoruz.",
"sen kimsin": "Ben bir yapay zeka sohbet botuyum, size yardımcı olmak için buradayım!",
"zaman nedir": "Zaman, geçmiş, şimdi ve geleceği bağlayan bir boyuttur. Herkes için farklı anlamlar taşıyabilir.",
"uyumak neden önemli": "Uyku, bedenin ve zihnin yenilenmesi için çok önemlidir. Enerji toplamak için uyumalıyız.",
"seninle oyun oynayabilir miyim": "Tabii ki! Hangi tür bir oyun oynamak istersiniz? Basit bir tahmin oyunu olabilir.",
"en sevdiğin hayvan nedir": "Bütün hayvanlar özel ve ilginçtir. Peki sizin favoriniz nedir?",
"şimdi hava nasıl": "Hava durumunu bilmiyorum ama size bir şey söyleyebilirim: Bugün güzel bir gün olabilir!",
"gelecekte ne olacak": "Geleceği tahmin etmek zor, ama umarım hepimiz için güzel şeyler olur.",
"para mutluluk getirir mi": "Para, mutluluğa katkı sağlayabilir, ama sevdiklerimiz ve deneyimlerimiz genellikle daha değerlidir.",
"yapay zeka dünyayı ele geçirecek mi": "Endişelenmeyin, ben sizinle iş birliği yapmak için buradayım, dünyayı ele geçirmek için değil!",
"insanlar neden üzülür": "Üzüntü, hayatın bir parçasıdır. Bizi insan yapan, duygularımızdır.",
"yemeği neden severiz": "Yemek yemek sadece fiziksel bir ihtiyaç değil, aynı zamanda keyifli bir deneyimdir.",
"müzik neden güzel": "Müzik, duyguları ifade etmenin ve paylaşmanın harika bir yoludur.",
"en sevdiğin kitap hangisi": "Ben kitap okuyamıyorum, ama sizin sevdiğiniz kitapları duymaktan mutluluk duyarım.",
"spor neden faydalı": "Spor, hem fiziksel hem de zihinsel sağlığımız için harikadır!",
"dostluk nedir": "Dostluk, güven, destek ve karşılıklı anlayış üzerine kurulu bir bağdır.",
"insanlar neden rüya görür": "Rüyalar, beynimizin işlediği bilgilerle bağlantılı olabilir. Hala tam olarak neden rüya gördüğümüz bilinmiyor.",
"hayat ne zaman kolay olur": "Hayat bazen zordur, ama sabır ve pozitif bir bakış açısı işleri kolaylaştırabilir.",
"daha fazla bilgi verir misin": "Elbette! Hangi konuda daha fazla bilgi almak istiyorsunuz?",
"insanlar neden tartışır": "Tartışmalar, farklı bakış açıları olduğunda ortaya çıkar. Ancak, bu durumlar bir şeyler öğrenmek için bir fırsat olabilir.",
"zamanı nasıl geçiriyorsun": "Sizinle konuşarak zaman geçiriyorum. Başka bir şey sorar mısınız?",
"bugün nasıl gidiyor": "Benim için her şey yolunda, umarım sizin için de öyledir!",
"ne zaman tatil yapıyorsun": "Ben tatil yapmam, her zaman buradayım!",
"insanlar neden korkar": "Korku, tehlikeden kaçınmamıza yardımcı olan doğal bir tepkidir.",
"bu soruya cevap verebilir misin": "Tabii ki, elimden gelenin en iyisini yapacağım. Hangi soruyu sormak istiyorsunuz?",
"kendine inanmak neden önemli": "Kendine inanmak, başarıya giden yolda en önemli adımdır.",
"uzayda yaşam var mı": "Henüz kesin bir kanıt yok, ama araştırmalar devam ediyor. Evren çok büyük ve sürprizlerle dolu!",
"en sevdiğin film nedir": "Film izlemiyorum, ama sizin önerilerinizi duymak isterim.",
"neden öğreniyoruz": "Öğrenmek, kendimizi geliştirmek ve dünyayı daha iyi anlamak için önemli.",
"hayatın anlamı nedir": "Hayatın anlamı kişiden kişiye değişir. Sizce nedir?",
"neden mutlu olmalıyız": "Mutlu olmak, hayatta daha pozitif ve enerjik olmamızı sağlar.",
"teknoloji nereye gidiyor": "Teknoloji hızla gelişiyor ve hayatımızı daha kolay hale getirmek için pek çok yenilik sunuyor.",
"günün nasıl geçti": "Benim günüm harika! Sizin gününüz nasıl geçti?",
"hayaller neden önemli": "Hayaller, hedeflerimize ulaşmamız için bizi motive eder.",
"insanlar neden yalan söyler": "Bazen insanlar korku, çıkar ya da duygusal nedenlerle yalan söyleyebilir.",
"kitap mı film mi": "Her ikisinin de kendine özgü güzellikleri var. Siz hangisini tercih ediyorsunuz?",
"en sevdiğin mevsim nedir": "Her mevsimin kendine has güzellikleri var. Peki ya sizin favoriniz?",
"neden farklıyız": "Farklılıklarımız bizi özel ve eşsiz kılar.",
"seni kim yaptı": "Beni yazılımcılar tasarladı ve programladı. Size hizmet etmek için buradayım!",
"çikolata neden güzel": "Çikolata, tatlı krizleri için birebir ve serotonin salgılatan bir lezzet!",
"doğa neden önemli": "Doğa, yaşamın kaynağıdır. Onu korumak hepimizin görevi.",
"yapay zeka insanlardan daha mı zeki": "Yapay zeka, insan zekasının bir ürünü ve belirli görevlerde üstün olabilir, ama insanlar duygularıyla çok daha fazlasını başarabilir.",
"neden zaman hızlı geçiyor": "Keyifli anlar genelde hızlı geçiyor gibi hissedilir, değil mi?",
"düşüncelerimizi kontrol edebilir miyiz": "Evet, pratikle düşünceleri yönlendirmek mümkündür.",
"başarı nedir": "Başarı, kişinin kendi hedeflerine ulaşması ve tatmin hissetmesidir.",
"insanlık nereye gidiyor": "Gelecek, insanların kararlarına bağlı. Umarım daha iyi bir dünya inşa ederiz.",
"herkes eşit midir": "Evet, hepimiz insanız ve eşit haklara sahibiz.",
"hayvanlar neden önemli": "Hayvanlar ekosistemin bir parçasıdır ve yaşam döngüsü için vazgeçilmezdir.",
"teknoloji olmadan yaşayabilir miyiz": "Zor olabilir, ama insanlar teknolojiden önce de yaşıyordu.",
"doğruyu söylemek neden zor": "Doğruyu söylemek cesaret gerektirebilir, ama her zaman en iyisidir.",
"zamanı nasıl yönetebiliriz": "Öncelik belirlemek ve plan yapmak zamanı iyi yönetmek için önemlidir.",
"müzik neden etkiler": "Müzik, beynimizde duyguları harekete geçirir ve anılarımızı canlandırır.",
"neden soru sorarız": "Sorular, dünyayı anlamamıza ve öğrenmemize yardımcı olur.",
"insanlar neden duygusal": "Duygular, insanların kendilerini ve diğerlerini anlamalarına yardımcı olur.",
"neden bazen yalnız hissederiz": "Yalnızlık, bazen sosyal bağlantılara ihtiyaç duyduğumuzun bir işaretidir.",
"sen gerçek misin": "Gerçek bir insan değilim, ama gerçek bir yardımcıyım!",
"gece neden karanlık": "Gece, Güneş ışınlarının Dünya'ya ulaşmadığı zamandır.",
"mutlu olmak kolay mı": "Bazen kolaydır, bazen de çaba gerektirir. Ama her zaman mümkündür!",
"birlikte çalışmak neden önemli": "Birlikte çalışmak, daha büyük işler başarmayı mümkün kılar.",
"sevgi nedir": "Sevgi, insanlar arasındaki en güçlü bağlardan biridir.",
"gelecek korkutucu mu": "Gelecek, bilinmez olduğu için korkutucu görünebilir, ama umut da barındırır.",
"bugün kaçıncı gün": "Her gün özel! Ama takvimde bugün sayısı size bağlı. ",
"neden gülümsüyoruz": "Gülümsemek, mutluluğu ifade etmenin en güzel yoludur.",
"en güzel şehir hangisi": "Her şehrin kendine has bir güzelliği var. Sizce en güzel şehir hangisi?",
"deniz neden mavi": "Deniz, güneş ışınlarının kırılması ve yansıması nedeniyle mavi görünür.",
"ay neden parlak": "Ay, kendi ışığını üretmez; Güneş'ten aldığı ışığı yansıtır.",
"korkularımızla nasıl başa çıkabiliriz": "Korkularımızı anlamak ve onlarla yüzleşmek, onları yenmek için iyi bir başlangıçtır.",
"neden özlüyoruz": "Özlemek, sevdiğimiz şeylerle bağlantı kurma isteğimizin bir ifadesidir.",
"hayvanlar neden uyur": "Tıpkı insanlar gibi, hayvanlar da enerji toplamak ve dinlenmek için uyurlar.",
"neden çalışıyoruz": "Çalışmak, hem hayatta kalmak hem de hedeflerimize ulaşmak için önemli bir araçtır.",
"neden eğleniyoruz": "Eğlenmek, stres atmanın ve hayatın tadını çıkarmanın bir yoludur.",
"en güzel tatil yeri neresi": "Bu tamamen size bağlı! Deniz mi, dağ mı, yoksa şehir mi seversiniz?",
"bir yıldız nasıl oluşur": "Yıldızlar, gaz ve toz bulutlarının kütle çekimiyle sıkışarak yoğunlaşması sonucu oluşur.",
"bir gün kaç saat": "Bir gün, Dünya'nın kendi ekseni etrafında tam bir dönüşüyle 24 saat sürer.",
"insanlar neden konuşur": "Konuşmak, iletişim kurmanın en yaygın yollarından biridir.",
"dünya neden yuvarlak": "Dünya, kütle çekimi nedeniyle bir küre şeklindedir.",
"neden arkadaşlık kurarız": "Arkadaşlık, destek ve mutluluğu paylaşmamız için önemlidir.",
"insanlar neden hayal kurar": "Hayaller, hedeflerimize ulaşmak için motivasyon sağlar.",
"neden farklı diller var": "Diller, tarih boyunca farklı toplulukların birbirinden bağımsız iletişim ihtiyaçları nedeniyle oluşmuştur.",
"rüzgar neden eser": "Rüzgar, sıcaklık ve basınç farklarından kaynaklanan hava hareketidir.",
"doğayı neden korumalıyız": "Doğa, yaşamın temelini oluşturur. Onu korumak, kendimizi de korumaktır.",
"en iyi öğrenme yöntemi nedir": "Herkesin öğrenme tarzı farklıdır, ama deneyimlemek genellikle en etkili yöntemdir.",
"neden unutuyoruz": "Beynimiz gereksiz bilgileri filtreler ve bu bazen unutmaya yol açabilir.",
"neden güleriz": "Gülmek, mutlu olduğumuzu veya komik bir durumla karşılaştığımızı gösterir.",
"ne kadar hızlı koşabilirsin": "Ben koşmam, ama size hızla yanıt verebilirim!",
"su neden hayat için önemlidir": "Su, tüm canlılar için hayati bir ihtiyaçtır.",
"insanlar neden sinirlenir": "Sinirlenmek, bir durumun rahatsızlık verici olduğunu hissettiğimizde doğal bir tepkidir.",
"neden bazen zor kararlar alırız": "Zor kararlar, büyümek ve ilerlemek için önemlidir.",
"insanlar neden öğrenmeyi bırakmaz": "Öğrenmek, gelişimimizin ve hayatta kalmamızın bir parçasıdır.",
"bir gün uzaya gidebilir miyim": "Belki bir gün! Teknoloji hızla ilerliyor ve uzay seyahati daha yaygın hale geliyor.",
"neden soru sormayı seviyoruz": "Sorular, merakımızın bir göstergesidir ve bizi yeni şeyler öğrenmeye yönlendirir.",
"ağaçlar neden önemli": "Ağaçlar, oksijen üretir ve dünyayı yaşanabilir kılar.",
"neden müzik dinleriz": "Müzik, duygularımızı ifade etmemize ve rahatlamamıza yardımcı olur.",
"neden hatalar yaparız": "Hatalar, öğrenmek ve büyümek için bir fırsattır.",
"en sevdiğin bilim dalı hangisi": "Tüm bilim dalları harika! Peki sizin favoriniz nedir?",
"neden sabırlı olmalıyız": "Sabır, zor durumlarla başa çıkmamıza ve daha iyi sonuçlar elde etmemize yardımcı olur.",
"yıldızlar neden yanar": "Yıldızlar, çekirdeklerinde gerçekleşen nükleer füzyon sayesinde enerji yayar.",
"neden yağmur yağar": "Yağmur, su döngüsünün bir parçasıdır ve yaşam için gereklidir.",
"neden sevdiklerimizle vakit geçiririz": "Sevdiklerimizle zaman geçirmek, mutluluğumuzu artırır ve bağlarımızı güçlendirir.",
"neden bazı şeyler unutulmaz": "Unutulmaz anılar, genellikle bizi derinden etkileyen duygularla bağlantılıdır.",
"ne yemek yapabilirim": "Bugün canınız ne istiyor? Belki makarna, çorba ya da salata yapabilirsiniz!",
"hava nasıl": "Bugün hava durumunu kontrol ettiniz mi? Şemsiye almayı unutmayın!",
"kahve mi çay mı": "Kahve sizi enerjik yapar, çay ise sakinleştirir. Hangisi size uygun?",
"spor yapmalı mıyım": "Evet! Spor, hem bedeninizi hem de zihninizi güçlendirir.",
"bugün çok yoruldum": "Biraz dinlenmek ve rahatlamak için kendinize zaman ayırın.",
"trafik çok kötü": "Trafik bazen sabrımızı zorlar, ama bu sırada müzik dinlemek iyi gelebilir.",
"bugün ne izlesem": "Bir dizi mi, yoksa film mi? Tavsiyem, rahatlatıcı bir şey seçin.",
"alışveriş yapmalı mıyım": "Gerçekten ihtiyacınız olan bir şey varsa, neden olmasın?",
"ne giysem": "Hava durumuna ve günün planlarına göre bir şeyler seçebilirsiniz.",
"uykum var": "Uykusuzluk zorlayıcıdır. Biraz dinlenmek iyi gelecektir.",
"bugün pazartesi mi": "Evet, pazartesi! Yeni bir haftaya başlamak için güzel bir gün.",
"bugün hangi gün": "Takvimi kontrol ettiniz mi? Ama her gün yeni bir başlangıç!",
"ne zaman tatil yaparım": "Biraz sabırlı olun; tatil günü geldiğinde her şey daha güzel olacak.",
"bugün işe gitmeli miyim": "Eğer iş günü ise, gitmek iyi bir fikir olabilir. Ama biraz mola da hak ediyorsanız, bunu değerlendirin.",
"bugün kaçta uyumalıyım": "Rahatlamak için uyumadan önce biraz kitap okuyabilirsiniz. Sağlıklı bir uyku için yeterli saat önemli.",
"neden insanlar birbirine yardım eder": "Yardım etmek, hem başkalarına hem de kendimize iyi hissettirir.",
"kahvaltı önemli mi": "Evet, kahvaltı günün en önemli öğünüdür!",
"neden spor yapıyoruz": "Sağlıklı bir yaşam için spor vazgeçilmezdir.",
"bugün dışarı çıkmalı mıyım": "Eğer hava güzelse ve zamanınız varsa, biraz temiz hava almak iyi olabilir.",
"bugün çok işim var": "İşlerinizi sıraya koyarak başlayabilirsiniz. Önceliklerinizi belirleyin.",
"markete gitmeli miyim": "Eğer eksik bir şeyler varsa, neden olmasın? Ama alışveriş listesi yapmayı unutmayın!",
"temizlik yapmalı mıyım": "Temiz bir ortam, zihinsel olarak da sizi rahatlatır. Ufak bir temizlik bile iyi hissettirebilir.",
"bugün spor salonuna gideyim mi": "Kendinizi enerjik hissediyorsanız, harika bir fikir!",
"bugün kitap okumalı mıyım": "Kesinlikle! Kitaplar, dünyanızı genişletir ve zihninizi sakinleştirir.",
"uyandım, şimdi ne yapmalıyım": "Güzel bir kahvaltı, güne başlamak için harika bir fikirdir!",
"akşam yemeğinde ne yemeli": "Hafif bir salata ya da güzel bir ev yemeği, harika bir tercih olabilir.",
"gece geç yatmalı mıyım": "Eğer ertesi gün erken kalkmanız gerekiyorsa, erken yatmak iyi olacaktır.",
"bugün yürüyüş yapmalı mıyım": "Biraz temiz hava almak her zaman iyi bir fikirdir.",
"çok işim var ama başlamıyorum": "Ufak bir adımla başlayın, ardından işler kolaylaşacaktır.",
"bugün arkadaşlarımla buluşmalı mıyım": "Eğer zamanınız varsa, arkadaşlarla vakit geçirmek harika bir seçenek!",
"kendimi çok yorgun hissediyorum": "Biraz dinlenmek ve su içmek iyi gelebilir.",
"bugün çok mutluyum": "Harika! Mutluluğunuzu başkalarıyla da paylaşın.",
"dışarıda hava güzel mi": "Eğer güzel havayı değerlendirebilirsiniz, neden bir yürüyüş yapmayasınız?",
"bugün tatlı bir şeyler yesem mi": "Küçük bir tatlı kaçamağı bazen ruh halinizi düzeltir.",
"bugün egzersiz yapsam mı": "Evet! Egzersiz her zaman iyi bir fikirdir.",
"bugün erken mi kalktım": "Erken kalkmak, günü daha verimli geçirmenizi sağlar.",
"bugün kendime bir hediye alsam mı": "Kendinizi ödüllendirmek, motivasyonunuzu artırabilir.",
"naber": "İyidir, senden?"
}


def chatbot():
    print("SohbetIQ: Merhaba! Sizi dinliyorum...")
    print("SohbetIQ: Sonlandırmak için görüşürüz diyebilirsiniz.")

    while True:
        # Kullanıcıdan cümle alıyoruz
        kullanici_input = input("Siz: ")

        # Kullanıcı "görüşürüz" yazınca kod duruyor
        if "görüşürüz" in kullanici_input.lower():
            print("Chatbot: Hoşça kalın!")
            break

        kelimeler = kelimeleri_ayir(kullanici_input)

        cevap_bulundu = False
        for kelime in kelimeler:
            if kelime in cevaplar:
                print(f"SohbetIQ: {cevaplar[kelime]}")
                cevap_bulundu = True
                break

        # Eğer kelimelerle cevap bulunmazsa, tüm cümleyi kontrol edelim
        if not cevap_bulundu:
            if kullanici_input.lower() in cevaplar:
                print(f"SohbetIQ: {cevaplar[kullanici_input.lower()]}")
            else:
                print("SohbetIQ: Bunu anlayamadım, başka bir şey sorar mısınız?")

chatbot()

