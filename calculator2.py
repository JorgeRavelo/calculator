import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.scroll = "auto"

    def add(e):
        try:
            result.value = f"Result: {float(num1.value) + float(num2.value)}"
        except:
            result.value = "Invalid input!"
        page.update()

    def subtract(e):
        try:
            result.value = f"Result: {float(num1.value) - float(num2.value)}"
        except:
            result.value = "Invalid input!"
        page.update()

    def multiply(e):
        try:
            result.value = f"Result: {float(num1.value) * float(num2.value)}"
        except:
            result.value = "Invalid input!"
        page.update()

    def divide(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            if n2 != 0:
                result.value = f"Result: {n1 / n2}"
            else:
                result.value = "Can't divide by 0!"
        except:
            result.value = "Invalid input!"
        page.update()

    num1 = ft.TextField(label="Number 1")
    num2 = ft.TextField(label="Number 2")
    result = ft.Text("Result: ", color="blue")

    tab1 = ft.Tab(
        text="Calculator",
        content=ft.Column([
            ft.Text("Basic Calculator", size=20, weight="bold"),
            num1,
            num2,
            ft.Row([
                ft.ElevatedButton("Add", on_click=add),
                ft.ElevatedButton("Subtract", on_click=subtract),
                ft.ElevatedButton("Multiply", on_click=multiply),
                ft.ElevatedButton("Divide", on_click=divide),
            ]),
            result
        ])
    )

    def calculate_bmi(e):
        try:
            w = float(weight.value)
            h = float(height.value) / 100
            bmi = w / (h * h)
            bmi_result.value = f"BMI: {round(bmi, 2)}"
        except:
            bmi_result.value = "Invalid input!"
        page.update()

    weight = ft.TextField(label="Weight (kg)")
    height = ft.TextField(label="Height (cm)")
    bmi_result = ft.Text("BMI: ", color="green")

    tab2 = ft.Tab(
        text="BMI",
        content=ft.Column([
            ft.Text("BMI Calculator", size=20, weight="bold"),
            weight,
            height,
            ft.ElevatedButton("Calculate BMI", on_click=calculate_bmi),
            bmi_result
        ])
    )

    tabs = ft.Tabs(tabs=[tab1, tab2])
    page.add(tabs)

ft.app(target=main)
