from guizero import *

app = App(title="Bài cáo IT",width=500,height=500,layout="auto",bg=(255,255,255))
text1 = Text(app,text="Xu Hướng Công Nghệ Thông Tin 2025",color=(0,0,139),size=20,font="Times New Roman")
picture = Picture(app,image="img/cntt.png")
text_box = Box(app,layout="auto",align="bottom",width="fill",height="fill")
text2 = Text(text_box,text="""Nội dung bài báo:

Hôm nay, chúng ta nói về các xu hướng công nghệ thông tin đang nổi bật trong năm 2024. Đầu tiên, trí tuệ nhân tạo (AI) tiếp tục là một trong những lĩnh vực phát triển mạnh mẽ nhất, với nhiều ứng dụng mới trong các ngành công nghiệp khác nhau.

AI không chỉ được sử dụng trong tự động hóa mà còn giúp cải thiện trải nghiệm người dùng, phân tích dữ liệu lớn, và thậm chí hỗ trợ ra quyết định trong kinh doanh.Thứ hai, điện toán đám mây (Cloud Computing) đang trở thành xu hướng chủ đạo, đặc biệt laf

trong bối cảnh các doanh nghiệp ngày càng phụ thuộc vào các dịch vụ dựa trên đám mây để tăng cường tính linh hoạt và tiết kiệm chi phí. Việc chuyển đổi từ hệ thống lưu trữ truyền thống sang điện toán đám mây đang diễn ra mạnh mẽ,

đặc biệt với sự ra đời của các nền tảng đa đám mây. Cuối cùng, bảo mật thông tin tiếp tục là một vấn đề quan trọng. Với sự gia tăng của các cuộc tấn công mạng, các doanh nghiệp đang đầu tư nhiều hơn vào việc bảo vệ dữ liệu và hệ thống của mình.

Các công nghệ như mã hóa, xác thực đa yếu tố, và giám sát an ninh mạng trở thành tiêu chuẩn bắt buộc. Xu hướng công nghệ thông tin này sẽ tiếp tục định hình cách chúng ta làm việc và sống trong những năm tới.""",color=(0,0,0),size=10)

app.display()
