import flet as ft

def main(page: ft.Page):
    page.title = "Multi-Tab Calculator"
    page.scroll = "auto"


    def do_basic_calc(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            if ops_dropdown.value == "+":
                res1.value = f"Result: {n1 + n2}"
            elif ops_dropdown.value == "-":
                res1.value = f"Result: {n1 - n2}"
            elif ops_dropdown.value == "*":
                res1.value = f"Result: {n1 * n2}"
            elif ops_dropdown.value == "/":
                if n2 != 0:
                    res1.value = f"Result: {n1 / n2}"
                else:
                    res1.value = "Can't divide by 0!"
        except:
            res1.value = "Invalid input!"
        page.update()

    num1 = ft.TextField(label="Number 1", width=150)
    num2 = ft.TextField(label="Number 2", width=150)
    ops_dropdown = ft.Dropdown(
        label="Operation",
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ],
    )
    calculo = ft.ElevatedButton("Calculate", onclick=do_basic_calc)
    res1 = ft.Text(value="Result: ", color="blue")

    tab1 = ft.Tab(
        text="Basic Calc",
        content=ft.Column([
            ft.Text("Basic Calculator", size=20, weight="bold"),
            num1,
            num2,
            ops_dropdown,
            calculo,
            res1
        ])
    )

    def do_bmi(e):
        try:
            w = float(weight.value)
            h = float(height.value) / 100 
            bmi = w / (h ** 2)
            res2.value = f"BMI: {round(bmi, 2)}"
        except:
            res2.value = "Invalid input!"
        page.update()

    weight = ft.TextField(label="Weight (kg)")
    height = ft.TextField(label="Height (cm)")
    bmi_btn = ft.ElevatedButton("Calculate BMI", onclick=do_bmi)
    res2 = ft.Text("BMI: ", color="green")

    tab2 = ft.Tab(
        text="BMI",
        content=ft.Column([
            ft.Text("BMI Calculator", size=20, weight="bold"),
            weight,
            height,
            bmi_btn,
            res2
        ])
    )

    def do_convert(e):
        try:
            val = float(input_val.value)
            from_u = from_unit.value
            to_u = to_unit.value
            result = "Invalid"
            if from_u == "cm" and to_u == "inch":
                result = val / 2.54
            elif from_u == "inch" and to_u == "cm":
                result = val * 2.54
            elif from_u == "kg" and to_u == "lb":
                result = val * 2.20462
            elif from_u == "lb" and to_u == "kg":
                result = val / 2.20462
            else:
                result = "Can't convert these units."
            res3.value = f"Result: {round(result, 2)}"
        except:
            res3.value = "Bad input"
        page.update()

    input_val = ft.TextField(label="Enter value")
    from_unit = ft.Dropdown(
        label="From",
        options=[
            ft.dropdown.Option("cm"),
            ft.dropdown.Option("inch"),
            ft.dropdown.Option("kg"),
            ft.dropdown.Option("lb"),
        ],
    )
    to_unit = ft.Dropdown(
        label="To",
        options=[
            ft.dropdown.Option("cm"),
            ft.dropdown.Option("inch"),
            ft.dropdown.Option("kg"),
            ft.dropdown.Option("lb"),
        ],
    )
    convert_btn = ft.ElevatedButton("Convert!", on_click=do_convert)
    res3 = ft.Text("Result: ", color="purple")

    tab3 = ft.Tab(
        text="Unit Convert",
        content=ft.Column([
            ft.Text("Unit Converter", size=20, weight="bold"),
            input_val,
            from_unit,
            to_unit,
            convert_btn,
            res3
        ])
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[tab1, tab2, tab3],
        expand=1
    )

    page.add(tabs)

ft.app(target=main)
