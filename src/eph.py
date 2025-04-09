def add_columns_header(header, *args):
    """
    Agrega columnas a una lista.

    Args:
    :param header: Lista a la que se le agregarán las columnas.
    :param *args: Columnas a agregar.
    """

    header.extend(args)


def add_data_ch04str(row):
    """
    Agrega la clasificación Masculino/Femenino a la columna ch4_str.

    Args:
    :param row: Fila a la que se le agregarán las columnas.
    """

    # Verifica si la columna 'CH04_str' ya existe en la fila
    if not 'CH04_str' in row:
        return

    if row["CH04"] == "1":
        row["CH04_str"] = "Masculino"
    else:
        row["CH04_str"] = "Femenino"


def add_data_nivel_ed_str(row):
    """
    Agrega la clasificación de nivel educativo a la columna nivel_ed_str.

    Args:
    :param row: Fila a la que se le agregarán las columnas.
    """

    # Verifica si la columna 'NIVEL_ED_str' ya existe en la fila
    if not 'NIVEL_ED_str' in row:
        return

    match row["NIVEL_ED"]:
        case "1":
            row["NIVEL_ED_str"] = "Primario incompleto"
        case "2":
            row["NIVEL_ED_str"] = "Primario completo"
        case "3":
            row["NIVEL_ED_str"] = "Secundario incompleto"
        case "4":
            row["NIVEL_ED_str"] = "Secundario completo"
        case "5" | "6":
            row["NIVEL_ED_str"] = "Superior o universitario"
        case "7" | "9":
            row["NIVEL_ED_str"] = "Sin Información"


def add_data_cond_lab(row):
    """
    Agrega la clasificación de condición laboral a la columna CONDICION_LABORAL.

    Args:
    :param row: Fila a la que se le agregarán las columnas.
    """

    # Verifica si la columna 'CONDICION_LABORAL' ya existe en la fila
    if not 'CONDICION_LABORAL' in row:
        return

    estado = int(row["ESTADO"])
    cat_ocup = int(row["CAT_OCUP"])

    if estado == 1 and cat_ocup in (1, 2):
        row["CONDICION_LABORAL"] = "Ocupado autónomo"
    elif estado == 1 and cat_ocup in (3, 4, 9):
        row["CONDICION_LABORAL"] = "Ocupado dependiente"
    elif estado == 2:
        row["CONDICION_LABORAL"] = "Desocupado"
    elif estado == 3:
        row["CONDICION_LABORAL"] = "Inactivo"
    else:
        row["CONDICION_LABORAL"] = "Fuera de categoría/sin información"


def add_data_universitario(row):
    """
    Agrega la clasificación de nivel universitario a la columna UNIVERSITARIO.

    Args:
    :param row: Fila a la que se le agregarán las columnas.
    """

    # Verifica si la columna 'UNIVERSITARIO' ya existe en la fila
    if not 'UNIVERSITARIO' in row:
        return

    if int(row["CH06"]) < 18:  # CH06 es la edad
        row["UNIVERSITARIO"] = 2
        return

    level = int(row["CH12"])

    if level == 8 or level == 7 and row["CH13"] == "1":
        row["UNIVERSITARIO"] = 1
    else:
        row["UNIVERSITARIO"] = 0


def imprimir_alfabetizadas(diccionario):
    """
    Imprime la cantidad de personas alfabetizadas por año.

    Args:
    :param diccionario: Diccionario con los datos de alfabetización.
    """

    print("Año\tAlfabetizados\tNo alfabetizados")
    for key, value in diccionario.items():
        print(f"{key}\t{value['A']}\t\t{value['NA']}")


def cant_personas_alfabetizadas(csv_reader):
    """
    Cuenta la cantidad de personas alfabetizadas en el archivo CSV por año.
    Se clasifican a las personas que tengan 2 años o más.

    Args:
    :param csv_reader: Lector CSV.
    """

    # Inicializa el contador
    count = {}

    # Itera sobre cada fila del lector CSV
    for row in csv_reader:

        # Si el año no existe, lo crea
        if row["ANO4"] not in count:
            count[row["ANO4"]] = {"A": 0, "NA": 0}

        # Analiza solo si está en el trimestre 4 y edad mayor a 2 años
        # Se usa 3 para la prueba NO OLVIDAR DE CAMBIAR
        if row["CH09"] != "3" and row["TRIMESTRE"] == "3":
            if row["CH09"] == "1":
                count[row["ANO4"]]["A"] += int(row["PONDERA"])
            else:
                count[row["ANO4"]]["NA"] += int(row["PONDERA"])

    imprimir_alfabetizadas(count)


def porc_extranjero_universitario(anio, trim, csv_reader):

    count = {"argentino": 0, "extranjero": 0}

    for row in csv_reader:
        if row["ANO4"] == anio and row["TRIMESTRE"] == trim and row["NIVEL_ED_str"] == "Superior o universitario":
            if int(row["CH15"]) in (4, 5):
                count["extranjero"] += int(row["PONDERA"])
            else:
                count["argentino"] += int(row["PONDERA"])

    porcentaje = (count["extranjero"] /
                  (count["argentino"] + count["extranjero"])) * 100

    print(
        f"El % de personas extranjeras que han cursado el nivel superior o universitario en el trimestre {trim} del año {anio} es del: {porcentaje:.2f}%")
