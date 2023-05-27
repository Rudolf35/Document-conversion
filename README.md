# Document-conversion
My first OpenCV project - Document image conversion

This project convert a document image file into a document file using OpenCV.

The program converts images in the following order.

1. 흑백 변환과 가우시안 블러 적용 후 캐니 엣지를 통해 경계 검출
2. 해당 이미지에 대해 findContours()로 컨투어를 찾아 가장 큰 컨투어를 골라서 꼭지점 추출
3. 추출한 꼭지점을 이용해 문서 부분만 이미지로 추출
4. 추출된 이미지에 적응형 가우시안 스레쉬홀딩을 적용해 바이너리 이미지로 변환
5. 테서렉트 OCR을 이용해서 텍스트 추출

sample document image file :
![image](https://github.com/Rudolf35/Document-conversion/assets/71507364/efe959cd-197e-45a6-93ea-6cc7df9138c4)

converted image file(Extract only the document part) :
![scan](https://github.com/Rudolf35/Document-conversion/assets/71507364/10a35f62-a91e-40d4-8caa-9022d29535af)

converted txt file :
[document.txt](https://github.com/Rudolf35/Document-conversion/files/11582181/document.txt)


reference : https://cori.tistory.com/132
