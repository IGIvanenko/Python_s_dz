def process_fractions(frac1_str, frac2_str):
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))
                                                    #сумма
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    prod_frac_num = num1 * num2                      #произведение
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac
