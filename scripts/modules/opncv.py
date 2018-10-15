import cv2
import numpy as np
import csv
point=[]
def opncv(video):
	#file_name='images_'+str(video)
	file_name='output'
	#自作フィルター
	def filt(src,median):
		b, g, r = src[:,:,0], src[:,:,1], src[:,:,2]
		mb,mg,mr=median[:,:,0], median[:,:,1], median[:,:,2]
		resalt=(b*0.114*64)/(mb*0.114)+(g*0.587*64)/(mg*0.587)+(r*0.299*64)/(mr*0.299)

		return resalt

	#メディアン&自作フィルター
	def medfilt(i,file_name):

		#画像読み込み
		img=cv2.imread(str(file_name)+'/'+str(i+1)+'.jpg')

		#メディアンフィルター
		median=cv2.medianBlur(img,21)
		cv2.imwrite(str(file_name)+'/'+'median'+str(i+1)+'.jpg',median)

		#自作フィルター
		resalt=filt(img,median)
		cv2.imwrite(str(file_name)+'/'+'resalt'+str(i+1)+'.jpg',resalt)

	#メディアン&ラプラシアンフィルター
	def medlap(i,file_name):

		#画像読み込み
		img=cv2.imread(str(file_name)+'/'+str(i+1)+'.jpg')

		#グレーフィルター
		gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

		#メディアンフィルター
		median=cv2.medianBlur(gray,41)
		cv2.imwrite(str(file_name)+'/'+'median'+str(i+1)+'.jpg',median)

		#ラプラシアンフィルター
		FILE_LAPLACIAN_5x5 = str(file_name)+'/'+"laplacian5x5"+str(i+1)+'.jpg'
		kernel_laplacian_5x5 = np.array([
                            [-1, -3, -4, -3, -1],
                            [-3,  0,  6,  0, -3],
                            [-4,  6, 24,  6, -4],
                            [-3,  0,  6,  0, -3],
                            [-1, -3, -4, -3, -1]
                            ], np.float32)
		img_laplacian_5x5 = cv2.filter2D(median, -1, kernel_laplacian_5x5)
		cv2.imwrite(FILE_LAPLACIAN_5x5, img_laplacian_5x5)

		thresh=100
		max_pixel=255
		ret,img_dst=cv2.threshold(img_laplacian_5x5,thresh,max_pixel,cv2.THRESH_BINARY)

		FILE_BIN=str(file_name)+'/'+"Bin"+str(i+1)+'.jpg'
		cv2.imwrite(FILE_BIN,img_dst)

	def lap_bin(i,file_name):

		#画像読み込み
		img=cv2.imread(str(file_name)+'/'+str(i+1)+'.jpg')

		#グレーフィルター
		gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

		height,width,ch = img.shape

		size = width*height

		#ラプラシアンフィルター
		FILE_LAPLACIAN_5x5 = str(file_name)+'/'+"laplacian5x5"+str(i+1)+'.jpg'
		kernel_laplacian_5x5 = np.array([
                            [-1, -3, -4, -3, -1],
                            [-3,  0,  6,  0, -3],
                            [-4,  6, 22,  6, -4],
                            [-3,  0,  6,  0, -3],
                            [-1, -3, -4, -3, -1]
                            ], np.float32)
		img_laplacian_5x5 = cv2.filter2D(gray, -1, kernel_laplacian_5x5)

		none = cv2.fastNlMeansDenoising(img_laplacian_5x5,None,255,7,21)

		thresh=160
		max_pixel=255
		ret,img_dst=cv2.threshold(none,thresh,max_pixel,cv2.THRESH_BINARY)

		FILE_BIN=str(file_name)+'/'+"Bin"+str(i+1)+'.jpg'
		cv2.imwrite(FILE_BIN,img_dst)





		white = cv2.countNonZero(img_dst)
		per = ((white/size)*100)
		print(per)
		if per<92:
			point.append(i)
		csvlist.append(per)


	f=open('output.csv','w')
	writer=csv.writer(f,lineterminator='\n')
	csvlist=[]
	#動画の長さを計算
	cap = cv2.VideoCapture(str('../upload/'+str(video)))
	frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	fps = cap.get(cv2.CAP_PROP_FPS)
	video_len_sec = frame / fps

	#画像一枚ごとにフィルタ処理
	for i in range(int(video_len_sec*10)):

		#メディアン&自作フィルター
		#medfilt(i,file_name)

		#メディアン&ラプラシアンフィルター
		#medlap(i,file_name)
		#print(str(i)+" correct")

		lap_bin(i,file_name)
	writer.writerow(csvlist)
	f.close()

	return point
