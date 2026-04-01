import asyncio
from llama_parse import LlamaParse

async def main():
    parser = LlamaParse(
        api_key="llx-LBEZLyOGBU6p1956H38xfULZIWn7VSPGLDdoML91BUWE08Iz",  # Lấy tại cloud.llamaindex.ai
        result_type="markdown",    
        num_workers=4,            
        verbose=True,
        parsing_instruction="Đây là văn bản hành chính. Hãy trích xuất toàn bộ nội dung, bao gồm cả quốc hiệu, tiêu ngữ và các thông tin ở đầu trang. Không được lược bỏ bất kỳ dòng nào.",
        language="vi"                
    )

    # Đưa đường dẫn file PDF "khó" nhất của bạn vào đây
    documents = await parser.aload_data("./1.jpg")

    # Ghi kết quả ra Markdown để kiểm tra độ chính xác của bảng biểu/text
    with open("result.md", "w", encoding="utf-8") as f:
        for i, doc in enumerate(documents):
            f.write(f"--- PAGE {i+1} ---\n")
            f.write(doc.text)
            f.write("\n\n")

    print("Xong! Bạn mở file result.md lên check độ chuẩn nhé.")

if __name__ == "__main__":
    asyncio.run(main())