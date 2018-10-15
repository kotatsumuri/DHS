import ffmpeg
import os
import shutil

def vi_clp(name):
	vidio=str(name)

	new_dir_path='output'
	if os.path.isdir(new_dir_path): #同じパス名のフォルダがある場合削除
		shutil.rmtree(new_dir_path)

	os.mkdir(new_dir_path) #フォルダ作成
	# 入力
	stream = ffmpeg.input('../upload/'+str(vidio))

	# 出力
	stream = ffmpeg.output(stream, str(new_dir_path)+'/%d.jpg',r=10 ,f='image2')

	# 実行
	ffmpeg.run(stream)
