# dikodekan oleh: salism3
# 22 - 07 - 2020 12:19

import os, random, time, sys, shutil
dari glob import glob
dari getpass import getpass

mencoba:
	impor facebookparser sebagai fb
	dari tindakan impor facebookparser
	dari colorama import init, Fore, Back
	init (autoreset = True)
kecuali ImportError:
	print ("Memasang modul ...")
	os.system (("python" if os.name == "nt" else "python3") + "-m permintaan pemasangan pip bs4 colorama")
	keluar ("\ nSukses")

B = Fore.BLUE
W = Kedepan PUTIH
C = Kedepan.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Kedepan. KUNING
ERR = f "{R} [!] {W}" 
ANTRIAN = f "{C} [?] {W}"
INF = f "{C} [+] {W}" 
DAN = f "{R} [!]"

TOTAL_ENTER = 0

ses = Tidak ada

list_menu = {
	"Suka": [
		"Spam Seperti di Rumah",
		"Spam Seperti di Garis Waktu Orang",
		"Spam Suka di Grup", 
		"Spam Seperti di Halaman Penggemar"
	],
	"reaksi": [
		"Spam React in Home",
		"Spam React in People Timeline",
		"Spam React in Group",
		"Spam React in Fanspage"
	],
	"komentar": [
		"Komentar Spam di Rumah",
		"Komentar Spam di Garis Waktu Orang",
		"Komentar Spam di Grup",
		"Komentar Spam di Halaman Penggemar"
	],
	"orang-orang": [
		"Terima Massal Permintaan Pertemanan" + DAN,
		"Tolak Massal Permintaan Pertemanan" + DAN,
		"Mass Unadd (bukan Unfriend)",
		"Mass Unfriend" + DAN,
		"Mass Follow Friend",
		"Mass Unfollow Friend",
	],
	"grup": [
		"Mass Leave Group" + DAN,
	],
	"chat": [
		"Teman Obrolan Massal",
		"Teman Obrolan Massal Online",
	],
	"pengunduh": [
		"Album Downloader",
		"Unduh Massal Foto di Kotak Masuk"
	],
	"penghapus": [
		"Obrolan Hapus Massal" + DAN,
		"Hapus Massal Posting" + DAN,
		"Mass Untag" + DAN,
		"Mass Tidak Seperti / Posting Tidak Bereaksi"
	],
	"lainnya": [
		"Temukan Id Orang",
		"Temukan Grup Id",
		"Hapus Folder Output Kosong",
		"Hapus Semua Output",
	],
	"tidak bereaksi": [
		"Tidak Seperti Massa / Tidak Bereaksi di Garis Waktu Orang",
		"Tidak Seperti Massal / Tidak Bereaksi di Halaman Penggemar"
	]
}


LOGO = f "" " 
  __ _ _
 _ __ __ _ / _| (_) __  ___ __ __  ____  __  ___ ___  _ __ ___
| '__/ _` | |_| | | \ \/ / '_ \\ \/ /\ \/ / / __/ _ \| '_ ` _ \
| | | (_| |  _| | |  >  <| | | |>  <  >  < | (_| (_) | | | | | |
|_|  \__,_|_| |_|_| /_/\_\_| |_/_/\_\/_/\_(_)___\___/|_| |_| |_|
  "" "

def updateFunc (func):
	def batin ():
		CURRENT_FUNC global
		CURRENT_FUNC = func
		func ()
	kembali ke dalam

def randomstring (num):
	char = list ("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM")
	rv = "" .join ([random.choice (char) untuk _ dalam rentang (num)])
	kembali rv

def spanduk ():
	os.system ("cls" if os.name == "nt" else "clear")
	cetak (LOGO)
	print ("" + Back.BLUE + Fore.BLACK + random.choice (["Subscribe: https://www.youtube.com/c/raflypakei2002"]))
	mencetak()

def input_ (teks, que = True, looping = True):
	jika perulangan:
		untuk _ dalam rentang (8):
			rv = masukan ((ANTRIAN jika que else "") + teks + C)
			jika rv.strip ():
				kembali rv
			lain:
				cetak (f "{R} [!] {W} masukan kosong \ n")
		lain:
			print (f "{R} [!] {W} Dah lah maless !!!")
			memasukkan()

	lain:
		masukan kembali ((QUE jika que else "") + teks + C)


def pilih (min, maks, teks = ">>>", error_msg = "input tidak valid", que = False):
	untuk _ dalam rentang (8):
		mencoba:
			data = int (input_ (W + teks, que = que, looping = False))
			jika data dalam jangkauan (min, max + 1):
				mengembalikan data
		kecuali ValueError:
			lulus
		cetak (f "{R} [!] {W} {error_msg} \ n")
	lain:
		print (f "{R} [!] {W} Dah lah maless !!!")
		memasukkan()

def confirm_execute ():
	text = "yes" + str (random.randint (0,999)). zfill (3)
	jika input_ (f "ketik '{text}' untuk mengonfirmasi:", looping = False)! = teks:
		cetak (ERR + "operasi dibatalkan!")
		memasukkan()

def check_login (cookie = Tidak ada):
	ses global
	jika bukan cookie:
		mencoba:
			cookies = open ("cookies.txt"). read ()
		kecuali:
			return False
	ses = fb.Account (cookie)
	kembali ses.logged

def show_select_menu (menu, back = True):
	untuk i, x di enumerate (menu):
		cetak (f "{C} {i + 1}). {W} {x}")

	jika kembali:
		cetak (f "{C} 0). {W} Kembali")

	kembali pilih (0 jika mundur lagi 1, len (menu))

# gunakan fungsi lambda untuk argumen dump_func
def dump (dump_func, limit, show_target = True):
	data = dump_func ()
	rv = data.items

	waktu tidur (1)
	mencetak()
	jika show_target:
		judul = data.bs4 (). temukan ("judul"). teks
		cetak (f "{INF} Target: {G} {judul [: 22]}")
	cetak (f "{INF} Mendapatkan data ...")

	jika bukan data.isNext atau len (rv)> batas:
		cetak (f "{INF} Total: {G} {len (rv [: limit])}")
		return rv [: limit]

	rv + = action.dump (data, limit = limit - len (rv))
	cetak (f "{INF} Total: {G} {len (rv [: limit])}")
	return rv [: limit]

proses def (func, list_, before_done = None):
	hitung = 0
	total = len (list_)
	untuk x dalam list_:
		hitung + = 1
		data = func (x)
		count_proccess (hitung, total)
		time.sleep (random.random () * random.randint (1,3))
	mencetak()
	jika dapat dihubungi (before_done):
		before_done ()
	cetak (INF + "Selesai!")
	memasukkan()

def count_proccess (hitung, total):
	angka = str (hitung * 100 / total)
	a, b = angka.split (".")

	angka = f "{a}. {b [: 2] .ljust (2, '')}%"

	sys.stdout.write (f "\ r {INF} Proses: {G} {angka} {W}")
	sys.stdout.flush ()

@update
def home ():
	spanduk()
	print (f "" "{C} 1). {W} Buka Menu
   {C} 2). {W} Masuk
   {C} 3). {W} Keluar
   {C} 4). {W} Perbarui
   {C} 0). {W} Keluar "" ")
	pilih = pilih (0,4)
	jika pilih == 0:
		spanduk()
		print ("Terima kasih telah menggunakan alat ini ^ _ ^")
	elif pilih == 1:
		jika tidak check_login ():
			print (ERR + "Anda harus login!")
			memasukkan()
		lain:
			Tidak bisa()
	elif pilih == 2:
		jika tidak check_login ():
			Gabung()
		lain:
			print (ERR + "Anda telah login!")
			memasukkan()
	elif pilih == 3:
		confirm_execute ()
		os.remove ("cookies.txt")
		memasukkan()
	elif pilih == 4:
		cetak (W + "\ n jika Anda menginstal alat ini dari git")
		print ("Anda bisa mengetik 'git pull'")

def login ():
	ses global
	os.system ("cls" if os.name == "nt" else "clear")
	cetak (f "" "               
			 {R} [PERINGATAN] {W}

   1. Khusus dewasa 18+
   2. Setelah berhasil login akun Anda akan
      mengomentari penulis secara otomatis
      foto profil dan reaksi
   3. Jangan gunakan ini untuk kejahatan
   4. Segala sesuatu yang dilakukan pengguna bukanlah tanggung jawab
      dari penulis
   5. Dengan menggunakan ini pengguna dianggap
      memahami dan mematuhi ketentuan di atas
      "" ")

	cookies = input _ ("Cookie Facebook Anda:")
	ses = fb.Account (cookie)
	mencoba:
		url = "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465"
		msg = ["Halo, Saya Pengguna RAFLY", "Halo bro gw pengguna Rafly btw toolnya keren banget", "jadilah dirimu sendiri dan jangan pernah menyerah"]
		action.status.comment (ses, url, random.choice (msg))
		waktu tidur (1)
		action.status.react (ses, url, type = random.choice (["wow", "love"]), in_reactions_picker = False)
	kecuali:
		lulus
	jika ses.logged:
		buka ("cookies.txt", "w"). tulis (cookie)
		print (f "{INF} Berhasil Masuk!")
		memasukkan()
	lain:
		cetak (ERR + "Cookies Not Valid!")
		memasukkan()

@update
menu def ():
	spanduk()
	print (f "Login as: {G} {ses.name [: 22]}")
	cetak (f "UID: {G} {ses.id} \ n")
	cetak (f "{C} Tidak. {W} Menu \ n {Y} --- ----")
	func = [like_menu, react_menu, comment_menu, people_menu, group_menu, chat_menu, downloader_menu, deleter_menu, other_menu]
	pilih = show_select_menu ([
		"Suka",
		"Reaksi", 
		"Komentar", 
		"Orang-orang", 
		"Kelompok", 
		"Obrolan", 
		"Pengunduh", 
		"Penghapus", 
		"Lain",
	])
	jika pilih == 0:
		rumah()
	lain:
		func [pilih - 1] ()

@update
def like_menu ():
	spanduk()
	menu_ = list_menu ["suka"]
	pilih = show_select_menu (menu_)
	show_target = Benar

	jika pilih == 0:
		Tidak bisa()
		keluar()

	spanduk()
	print (f "{C} Dipilih: {W} {menu_ [pilih - 1]} \ n")

	jika pilih == 1:
		func = lambda: fb.like_post_home (ses)
		show_target = False

	elif pilih == 2:
		target = input _ ("Id Orang:")
		func = lambda: fb.like_post_people (ses, target)

	elif pilih == 3:
		target = input _ ("Grup Id:")
		func = lambda: fb.like_post_group (ses, target)

	elif pilih == 4:
		target = input _ ("Halaman Penggemar Nama Pengguna:")
		func = lambda: fb.like_post_fanspage (ses, target)

	limit = pilih (1, 350, text = "Limit:", error_msg = "min: 1, max: 350", que = True)
	confirm_execute ()
	data = dump (func, limit, show_target = show_target)
	procces (lambda url: action.open_url (ses, url), data)

@update
def react_menu ():
	spanduk()
	menu_ = list_menu ["bereaksi"]
	type_react = ["love", "care", "haha", "wow", "sad", "angry"]
	pilih = show_select_menu (menu_)
	show_target = Benar

	jika pilih == 0:
		Tidak bisa()
		keluar()

	spanduk()
	print (f "{C} Dipilih: {W} {menu_ [pilih - 1]} \ n")

	jika pilih == 1:

		func = lambda: fb.react_post_home (ses)
		show_target = False

	elif pilih == 2:
		target = input _ ("Id Orang:")
		func = lambda: fb.react_post_people (ses, target)

	elif pilih == 3:
		target = input _ ("Grup Id:")
		func = lambda: fb.react_post_group (ses, target)

	elif pilih == 4:
		target = input _ ("Halaman Penggemar Nama Pengguna:")
		func = lambda: fb.react_post_fanspage (ses, target)

	limit = pilih (1, 350, text = "Limit:", error_msg = "min: 1, max: 350", que = True)
	react = show_select_menu (daftar (peta (lambda x: x.capitalize (), type_react)))
	react = type_react [bereaksi - 1]
	confirm_execute ()
	data = dump (func, limit, show_target = show_target)
	procces (lambda url: action.status.react (ses, url, type = react), data)

@update
def comment_menu ():
	spanduk()
	menu_ = list_menu ["komentar"]
	pilih = show_select_menu (menu_)
	show_target = Benar

	jika pilih == 0:
		Tidak bisa()
		keluar()

	spanduk()
	print (f "{C} Dipilih: {W} {menu_ [pilih - 1]} \ n")
	
	jika pilih == 1:
		func = lambda: fb.comment_post_home (ses)
		show_target = False

	elif pilih == 2:
		target = input _ ("Id Orang:")
		func = lambda: fb.comment_post_people (ses, target)
	
	elif pilih == 3:
		target = input _ ("Grup Id:")
		func = lambda: fb.comment_post_group (ses, target)

	elif pilih == 4:
		target = input _ ("Halaman Penggemar Nama Pengguna:")
		func = lambda: fb.comment_post_fanspage (ses, target)

	comment = input _ ("Komentar:")
	batas = pilih (1, 100, teks = "Batas:", error_msg = "min: 1, maks: 100", que = Benar)
	confirm_execute ()
	data = dump(func, limit, show_target = show_target)
	procces(lambda url: action.status.comment(ses, url, comment), data)

@updateFunc
def people_menu():
	banner()
	menu_ = list_menu["people"]
	pilih = show_select_menu(menu_)

	if pilih == 0:
		menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	if pilih == 1:
		func = lambda: fb.friend_request(ses)
		execute_func = lambda url: action.open_url(ses, url[0])

	elif pilih == 2:
		func = lambda: fb.friend_request(ses)
		execute_func = lambda url: action.open_url(ses, url[1])

	elif pilih == 3:
		func = lambda: fb.friend_requested(ses)
		execute_func = lambda url: action.open_url(ses, url)

	elif pilih == 4:
		func = lambda: fb.myFriend(ses)
		execute_func = lambda data: action.people.unfriend(ses, data[1])

	elif pilih == 5:
		func = lambda: fb.myFriend(ses)
		execute_func = lambda data: action.people.follow(ses, data[1])

	elif pilih == 6:
		func = lambda: fb.myFriend(ses)
		execute_func = lambda data: action.people.unfollow(ses, data[1])

	limit = select(1, 300, text = "Limit: ", error_msg = "min: 1, max: 300", que = True)
	confirm_execute()
	data = dump(func, limit, show_target = False)
	procces(execute_func, data)

@updateFunc
def group_menu():
	banner()
	menu_ = list_menu["group"]
	pilih = show_select_menu(menu_)

	if pilih == 0:
		menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	if pilih == 1:
		func = lambda: fb.myGroup(ses)
		execute_func = lambda data: action.group.leave_group(ses, data[1])

	limit = select(1, 200, text = "Limit: ", error_msg = "min: 1, max: 200", que = True)
	confirm_execute()
	data = dump(func, limit, show_target = False)
	procces(execute_func, data)

@updateFunc
def chat_menu():
	banner()
	menu_ = list_menu["chat"]
	pilih = show_select_menu(menu_)

	if pilih == 0:
		menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	if pilih == 1:
		func = lambda: fb.myFriend(ses)

	elif pilih == 2:
		func = lambda: fb.onlineFriend(ses)

	msg = input_("Message: ")
	limit = select(1, 100, text = "Limit: ", error_msg = "min: 1, max: 100", que = True)
	confirm_execute()
	data = dump(func, limit, show_target = False)
	procces(lambda data: action.people.send_msg(ses, data[1], msg), data)

@updateFunc
def downloader_menu():
	banner()
	menu_ = list_menu["downloader"]
	pilih = show_select_menu(menu_)
	folder = randomstring(10)

	if pilih == 0:
		menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	if pilih == 1:
		target = input_("Id People: ")
		album = fb.list_album(ses, target).items
		print(f"{INF}Select album:")
		pilih = show_select_menu([x[0] for x in album], back = False)

		album = album[pilih - 1][1]
		func = lambda: fb.list_photo_inAlbum(ses, album)


	elif pilih == 2:
		url = input_("Url Inbox (use mbasic): ")
		func = lambda: fb.get_photo_from_inbox(ses, url)

	limit = select(1, 99999, text = "Limit: ", error_msg = "min: 1, max: 99999", que = True)
	confirm_execute()
	data = dump(func, limit, show_target = False)
	os.mkdir("output/" + folder)
	procces(lambda url: open(f"output/{folder}/{randomstring(10)}.jpg", "wb").write(ses.session.get(url).content), data, before_done = lambda: print(f"{INF}file saved in folder: output/{folder}"))

@updateFunc
def deleter_menu():
	banner()
	menu_ = list_menu["deleter"]
	pilih = show_select_menu(menu_)

	if pilih == 0:
		menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	if pilih == 1:
		func = lambda: fb.msgUrl(ses)
		execute_func = lambda url: action.people.deleteMsg(ses, url)

	elif pilih == 2:
		func = lambda: fb.option_post_people(ses, "me")
		execute_func = lambda url: action.status.delete_post(ses, url)

	elif pilih == 3:
		func = lambda: fb.option_post_people(ses, "me")
		execute_func = lambda url: action.status.untag_post(ses, url)

	elif pilih == 4:
		unreact_submenu()
		exit()

	limit = select(1, 200, text = "Limit: ", error_msg = "min: 1, max: 200", que = True)
	confirm_execute()
	data = dump(func, limit, show_target = False)
	procces(execute_func, data)

@updateFunc
def unreact_submenu():
	banner()
	menu_ = list_menu["unreact"]
	pilih = show_select_menu(menu_)
	show_target = True

	if pilih == 0:
		deleter_menu()
		exit()

	banner()
	print(f"   {C}Selected:{W} {menu_[pilih - 1]}\n")

	# if pilih == 1:
	# 	func = lambda: fb.like_post_home(ses)
	# 	show_target = False

	if pilih == 1:
		target = input _ ("Id Orang:")
		func = lambda: fb.react_post_people (ses, target)

	# elif pilih == 3:
	# target = input _ ("Grup Id:")
	# func = lambda: fb.react_post_group (ses, target)

	elif pilih == 2:
		target = input _ ("Halaman Penggemar Nama Pengguna:")
		func = lambda: fb.react_post_fanspage (ses, target)

	limit = pilih (1, 350, text = "Limit:", error_msg = "min: 1, max: 350", que = True)
	confirm_execute ()
	data = dump (func, limit, show_target = show_target)
	procces (lambda url: action.status.react (ses, url, type = "unreact"), data)

@update
def other_menu ():
	spanduk()
	menu_ = list_menu ["lainnya"]
	pilih = show_select_menu (menu_)

	jika pilih == 0:
		Tidak bisa()
		keluar()

	spanduk()
	print (f "{C} Dipilih: {W} {menu_ [pilih - 1]} \ n")

	jika pilih == 1:
		text = input _ ("Nama Lengkap:")
		data = fb.find_people(ses, text)
		if not data:
			print(ERR + "Not Found!")
		else:
			print(f"{INF}Name: {data.name}")
			print(f"{INF}ID  : {data.id}")
	elif pilih == 2:
		text = input_("Full Name: ")
		data = fb.find_group(ses, text)
		if not data:
			print(ERR + "Not Found!")
		else:
			print(f"{INF}Name: {data.name}")
			print(f"{INF}ID  : {data.id}")
	elif pilih == 3:
		confirm_execute()
		data = glob("output/*")
		for x in data:
			if len(os.listdir(x)) == 0:
				os.rmdir(x)
		print(f"{INF}Done!")
	elif pilih == 4:
		confirm_execute()
		data = glob("output/*")
		for x in data:
			shutil.rmtree(x)
		print(f"{INF}Done!")

	enter()


CURRENT_FUNC = home

def enter():
	global TOTAL_ENTER
	TOTAL_ENTER += 1
	if TOTAL_ENTER > 8:
		exit()
	getpass(f"\n   {C}[{W} Press Enter to Back {C}]{W}")
	CURRENT_FUNC()
	exit()

try:
	home()
except KeyboardInterrupt:
	exit(ERR + "Exit: Ok")
except Exception as e:
	print(ERR + str(e))