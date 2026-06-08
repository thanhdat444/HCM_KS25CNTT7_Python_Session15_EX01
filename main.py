inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    global inventory_stock

    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def calculate_final_price(quantity, price):
    subtotal = quantity * price

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.1

    after_discount = subtotal - discount

    vat = after_discount * 0.08

    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def print_report():
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    global inventory_stock
    global total_revenue

    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print("\n--- NHẬP HÀNG ---")

                amount = input("Nhập số lượng sản phẩm muốn thêm: ").strip()

                if not amount.isdigit():
                    print("Dữ liệu phải là số!")
                    continue

                amount = int(amount)

                if amount <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                add_stock(amount)

            case "2":
                print("\n--- BÁN HÀNG ---")

                quantity = input("Nhập số lượng mua: ").strip()
                price = input("Nhập đơn giá ($): ").strip()

                try:
                    quantity = int(quantity)
                    price = float(price)
                except:
                    print("Dữ liệu phải là số!")
                    continue

                if quantity <= 0 or price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                if not process_sale(quantity):
                    continue

                subtotal, discount, vat, final_total = calculate_final_price(
                    quantity, price
                )

                inventory_stock -= quantity
                total_revenue += final_total

                print("-> Hóa đơn chi tiết:")
                print(f"Số lượng: {quantity} | Đơn giá: ${price}")
                print(f"Tạm tính: ${subtotal}")
                print(f"Giảm giá (10%): ${discount}")
                print(f"Thuế VAT (8%): ${vat}")
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công!")

            case "3":
                print_report()

            case "4":
                print("Lưu dữ liệu và thoát chương trình.")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()