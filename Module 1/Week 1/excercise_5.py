def md_nre_single_sample(y_true, y_pred, power_root, exponent):
    differential = abs(y_true ** (1 / power_root) - y_pred ** (1 / power_root))
    return differential ** exponent

print(md_nre_single_sample(y_true=100, y_pred=99.5, power_root=2, exponent=1))
print(md_nre_single_sample(y_true=50, y_pred=49.5, power_root=2, exponent=1))
print(md_nre_single_sample(y_true=20, y_pred=19.5, power_root=2, exponent=1))
print(md_nre_single_sample(y_true=0.6, y_pred=0.1, power_root=2, exponent=1))
