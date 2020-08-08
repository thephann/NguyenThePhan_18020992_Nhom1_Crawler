# Week3


Scrapy dùng để thu thập dữ liệu từ các trang web và trích xuất dữ liệu 

Các thành phần của scrapy gồm:
	Engine
	Scheduler
	Dowloader
	Spiders
	Item Pipeline
	Downloader middlewares

Spiders được viết bởi người sử dụng và là nơi xử lý , phân tích các yêu cầu và ,crawl dữ liệu.Cấu trúc một file trong spiders:
	name :tên của spider và không được đặt các name giống nhau
	allowed_domains:vùng cho phép crawl dữ liệu
	start_urls:
	hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:
	+kiểm tra xem link đó có phải là link cần crawk không (tránh crawl các link rác) 
	+Sau khi kiểm tra thì ghi lại :link,title,category,date,description,relatednews,content,tags và author
	yield from : cho phép chỉ tiến hành crawl trên các bài báo có miền https://vtc.vn/


Kết quả thu thập được:
	Nguồn: https://vtc.vn/
	Các thông tin thu thập: link,title,category,date,description,relatednews,content,tags và author
	Tình trạng:Đã thu thập xong 
	Số lượng: 3664 bài báo

