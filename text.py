class text:
  def supscr(x):
    normal = "abcxyz0123456789+-=()"
    super_s = "ᵃᵇᶜˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
  def subscr(x):
    normal = "aekmnx0123456789+-=()"
    sub_s = "ₐₑₖₘₙₓ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)
