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

    age = int(row["CH06"])

    if age < 18:
        row["UNIVERSITARIO"] = 2
    elif row["NIVEL_ED"] == "6":
        row["UNIVERSITARIO"] = 1
    else:
        row["UNIVERSITARIO"] = 0
