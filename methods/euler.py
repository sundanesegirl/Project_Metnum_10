def euler(f, x0, y0, h, xtarget):

    n = int((xtarget - x0) / h)

    x = x0
    y = y0

    tabel = []
    langkah_perhitungan = []

    for i in range(n):

        slope = f(x, y)

        y_baru = y + h * slope

        tabel.append({
            "iterasi": i + 1,
            "x": round(x, 6),
            "y": round(y, 6),
            "slope": round(slope, 6),
            "y_baru": round(y_baru, 6)
        })

        langkah = f"""
        ========================
        Iterasi {i+1}
        ========================

        f({round(x,6)}, {round(y,6)})
        = {round(slope,6)}

        y{i+1}
        = {round(y,6)} + ({h} × {round(slope,6)})
        = {round(y_baru,6)}
        """

        langkah_perhitungan.append(langkah)
        y = y_baru
        x = x + h

       
    return y, tabel, langkah_perhitungan