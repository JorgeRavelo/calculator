import flet as ft

def main(page: ft.Page):
    page.title = "Multi Calculator"
    page.scroll = "auto"

    def add(e):
        try:
            result.value = f"Result: {float(num1.value) + float(num2.value)}"
        except ValueError:
            result.value = "Invalid input!"
        page.update()

    def subtract(e):
        try:
            result.value = f"Result: {float(num1.value) - float(num2.value)}"
        except ValueError:
            result.value = "Invalid input!"
        page.update()

    def multiply(e):
        try:
            result.value = f"Result: {float(num1.value) * float(num2.value)}"
        except ValueError:
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
        except ValueError:
            result.value = "Invalid input!"
        page.update()

    num1 = ft.TextField(label="Number 1", keyboard_type=ft.KeyboardType.NUMBER)
    num2 = ft.TextField(label="Number 2", keyboard_type=ft.KeyboardType.NUMBER)
    result = ft.Text("Result: ", color=ft.Colors.BLUE_500)

    tab1 = ft.Tab(
        text="Basic",
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

    # BMI Calculator
    def calculate_bmi(e):
        try:
            w = float(weight.value)
            h = float(height.value) / 100
            bmi = w / (h * h)
            bmi_result.value = f"BMI: {round(bmi, 2)}"
        except ValueError:
            bmi_result.value = "Invalid input!"
        page.update()

    weight = ft.TextField(label="Weight (kg)", keyboard_type=ft.KeyboardType.NUMBER)
    height = ft.TextField(label="Height (cm)", keyboard_type=ft.KeyboardType.NUMBER)
    bmi_result = ft.Text("BMI: ", color=ft.Colors.GREEN_500)

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

    def convert_unit(e):
        try:
            val = float(unit_input.value)
            f = from_unit_text.value.lower().strip()
            t = to_unit_text.value.lower().strip()

            if f == t:
                unit_result.value = f"{val} {f} = {val} {t}"
            elif f == "cm" and t == "inches":
                unit_result.value = f"{val} cm = {round(val / 2.54, 2)} inches"
            elif f == "inches" and t == "cm":
                unit_result.value = f"{val} inches = {round(val * 2.54, 2)} cm"
            elif f == "kg" and t == "pounds":
                unit_result.value = f"{val} kg = {round(val * 2.20462, 2)} pounds"
            elif f == "pounds" and t == "kg":
                unit_result.value = f"{val} pounds = {round(val / 2.20462, 2)} kg"
            else:
                unit_result.value = "Invalid conversion! Supported: cm/inches, kg/pounds"
        except ValueError:
            unit_result.value = "Invalid input! Please enter numbers."
        except Exception as ex:
            unit_result.value = f"An unexpected error occurred: {ex}"
        page.update()

    unit_input = ft.TextField(label="Value to convert", keyboard_type=ft.KeyboardType.NUMBER)
    from_unit_text = ft.TextField(label="From Unit (e.g., cm, inches, kg, pounds)")
    to_unit_text = ft.TextField(label="To Unit (e.g., cm, inches, kg, pounds)")
    unit_result = ft.Text("Converted result will appear here.", color=ft.Colors.PURPLE_500)

    tab3 = ft.Tab(
        text="Unit Converter",
        content=ft.Column([
            ft.Text("Unit Converter", size=20, weight="bold"),
            unit_input,
            from_unit_text,
            to_unit_text,
            ft.ElevatedButton("Convert", on_click=convert_unit),
            unit_result,
            ft.Text("Supported conversions: cm/inches, kg/pounds", size=12, color=ft.Colors.GREY_600)
        ])
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[tab1, tab2, tab3]
    )
    page.add(tabs)

ft.app(target=main)