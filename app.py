from flask import Flask, render_template, request
from methods.euler import euler
from methods.heun import heun
from methods.rk3 import rk3 
from methods.rk4 import rk4
from sympy import symbols, sympify, lambdify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    hasil = None
    error = None

    if request.method == 'POST':

        fungsi = request.form['fungsi']
        x0 = request.form['x0']
        y0 = request.form['y0']
        h = request.form['h']
        xtarget = request.form['xtarget']
        metode = request.form['metode']

        if fungsi.strip() == "":
            error = "Fungsi tidak boleh kosong"
        
        elif float(h) <= 0:
            error = "Nilai h harus lebih besar dari 0"
        
        elif float(xtarget) <= float(x0):
            error = "x Target harus lebih besar dari x0"
        
         
        else:
            
            x, y = symbols('x y')
            expr = sympify(fungsi)
            f = lambdify((x, y), expr)

            hasil_euler_cmp, _, _ = euler(
            f, float(x0), float(y0),
            float(h), float(xtarget)
            )

            hasil_heun_cmp, _, _ = heun(
            f, float(x0), float(y0),
            float(h), float(xtarget)
            )

            hasil_rk3_cmp, _, _ = rk3(
            f, float(x0), float(y0),
            float(h), float(xtarget)
            )

            hasil_rk4_cmp, _, _ = rk4(
            f, float(x0), float(y0),
            float(h), float(xtarget)
            )


            if metode == "Euler":
             
                hasil_euler, _, _ = euler(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil_heun, _, _ = heun(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil_rk3, _, _ = rk3(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil_rk4, _, _ = rk4(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil_euler, tabel_euler, langkah_euler = euler(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil = {
                'fungsi': fungsi,
                'x0': x0,
                'y0': y0,
                'h': h,
                'xtarget': xtarget,
                'metode': metode,
                'hasil_euler': round(hasil_euler, 6),
                'tabel_euler': tabel_euler,
                'langkah_euler': langkah_euler,
                'perbandingan_euler': round(hasil_euler_cmp, 6),
                'perbandingan_heun': round(hasil_heun_cmp, 6),
                'perbandingan_rk3': round(hasil_rk3_cmp, 6),
                'perbandingan_rk4': round(hasil_rk4_cmp, 6),
                }

            elif metode == "Heun":
                x, y = symbols('x y')
                expr = sympify(fungsi)
                f = lambdify((x, y), expr)

                hasil_heun, tabel_heun, langkah_heun = heun(
                f,
                float(x0),
                float(y0),
                float(h),
                float(xtarget)
                )

                hasil = {
                'fungsi': fungsi,
                'x0': x0,
                'y0': y0,
                'h': h,
                'xtarget': xtarget,
                'metode': metode,
                'hasil_heun': round(hasil_heun, 6),
                'tabel_heun': tabel_heun,
                'langkah_heun': langkah_heun,
                'perbandingan_euler': round(hasil_euler_cmp, 6),
                'perbandingan_heun': round(hasil_heun_cmp, 6),
                'perbandingan_rk3': round(hasil_rk3_cmp, 6),
                'perbandingan_rk4': round(hasil_rk4_cmp, 6),
                }

            elif metode == "Runge-Kutta Orde 3":
                x, y = symbols('x y')
                expr = sympify(fungsi)
                f = lambdify((x, y), expr)

                hasil_rk3, tabel_rk3, langkah_rk3 = rk3(
                    f,
                    float(x0),
                    float(y0),
                    float(h),
                    float(xtarget)
                )

                hasil = {
                'fungsi': fungsi,
                'x0': x0,
                'y0': y0,
                'h': h,
                'xtarget': xtarget,
                'metode': metode,
                'hasil_rk3': round(hasil_rk3, 6),
                'tabel_rk3': tabel_rk3,
                'langkah_rk3': langkah_rk3,
                'perbandingan_euler': round(hasil_euler_cmp, 6),
                'perbandingan_heun': round(hasil_heun_cmp, 6),
                'perbandingan_rk3': round(hasil_rk3_cmp, 6),
                'perbandingan_rk4': round(hasil_rk4_cmp, 6),
                }

            elif metode == "Runge-Kutta Orde 4":
                x, y = symbols('x y')
                expr = sympify(fungsi)
                f = lambdify((x, y), expr)

                hasil_rk4, tabel_rk4, langkah_rk4 = rk4(
                f,
                float(x0),
                float(y0),
                float(h),
                float(xtarget)
                )
                
                hasil = {    
                'fungsi': fungsi,
                'x0': x0,
                'y0': y0,
                'h': h,
                'xtarget': xtarget,
                'metode': metode,
                'hasil_rk4': round(hasil_rk4, 6),
                'tabel_rk4': tabel_rk4,
                'langkah_rk4':langkah_rk4,
                'perbandingan_euler': round(hasil_euler_cmp, 6),
                'perbandingan_heun': round(hasil_heun_cmp, 6),
                'perbandingan_rk3': round(hasil_rk3_cmp, 6),
                'perbandingan_rk4': round(hasil_rk4_cmp, 6),
                }

    print("hasil")
    return render_template(
        'index.html',
        hasil=hasil,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)