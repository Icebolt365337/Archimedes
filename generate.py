import random
from fractions import Fraction
import math
from statistics import mode
from text import text

class generate:
  def basicop_problem():
    funcs = ["add", "sub", "mul", "div"]
    func = random.choice(funcs)
    if func == "add":
      a = random.randint(100, 999)
      b = random.randint(100, 999)
      d = str(a+b)
      a = str(a)
      b = str(b)
      c = "What is "+a+"+"+b+"?"
      return c, d
    if func == "sub":
      a = random.randint(501, 999)
      b = random.randint(100, 500)
      d = str(a-b)
      a = str(a)
      b = str(b)
      c = "What is "+a+" - "+b+"?"
      return c, d
    if func == "mul":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      d = str(a*b)
      a = str(a)
      b = str(b)
      c = "What is "+a+" x "+b+"?"
      return c, d
    if func == "div":
      a = random.randint(51, 99)
      d = random.randint(2, 10)
      b = str(a*d)
      a = str(a)
      b = str(b)
      c = "What is "+b+"/"+a+"?"
      return c, d

  def negative_problem():
    operations = ["addition", "subtraction", "multiplication", "division"]
    operation = random.choice(operations)
    if operation == "addition":
      a = random.randint(-99, -1)
      b = random.randint(-99, -1)
      d = str(a+b)
      a = str(a)
      b = str(b)
      e = "What is "+a+" plus "+b+"?"
    if operation == "subtraction": 
      a = random.randint(-99, -1)
      b = random.randint(-99, -1)
      d = str(a-b)
      a = str(a)
      b = str(b)
      e = "What is "+a+" minus "+b+"?"
    if operation == "multiplication": 
      a = random.randint(-12, -1)
      b = random.randint(-12, -1)
      d = str(a*b)
      a = str(a)
      b = str(b)
      e = "What is "+a+" x "+b+"?"
    if operation == "division": 
      a = random.randint(-12, -1)
      d = random.randint(-12, -1)
      b = str(a*d)
      a = str(a)
      d = str(d)
      e = "What is "+b+" divided by "+a+"?"
    return d, e

  def perimeter_problem():
    shapes = ["triangle", "square", "rectangle", "pentagon", "hexagon", "octagon", "circle"]
    shape = random.choice(shapes)
    a = random.randint(10, 99)
    if shape == "triangle":
      b = random.randint(10, 99)
      c = random.randint(10, 99)
      d = str(a+b+c)
      a = str(a)
      b = str(b)
      c = str(c)
      e = "What is the perimeter of a triangle with side lengths of "+a+", "+b+", and "+c+"?"
      f = "Since this is a triangle, we add all three sides together to get the perimeter. "+a+"+"+b+"+"+c+" = "+d+"."
    if shape == "square":
      d = str(4*a)
      a = str(a)
      e = "What is the perimeter of a square whose side lengths are "+a+"?"
      f = "Since this is a square, all four sides have the same side length. We can multiply one side length, "+a+", by four. 4 x "+a+" = "+d+"."
    if shape == "rectangle":
      b = random.randint(10, 99)
      d = str((2*a)+(2*b))
      a = str(a)
      b = str(b)
      e = "What is the perimeter of a rectangle whose side lengths are "+a+" and "+b+"?"
      f = "Since a rectangle has two pairs of matching sides, we can multiply each side length by 2 and add them together to get the perimeter. (2 x "+a+")+(2 x "+b+") = "+d+"."
    if shape == "pentagon":
      d = str(5*a)
      a = str(a)
      e = "What is the perimeter of a regular pentagon whose side lengths are "+a+"?"
      f = "Since this is a pentagon, all five sides have the same side length. We can multiply one side length, "+a+", by five. 5 x "+a+" = "+d+"."
    if shape == "hexagon":
      d = str(6*a)
      a = str(a)
      e = "What is the perimeter of a regular hexagon whose side lengths are "+a+"?"
      f = "Since this is a hexagon, all six sides have the same side length. We can multiply one side length, "+a+", by six. 6 x "+a+" = "+d+"."
    if shape == "octagon":
      d = str(8*a)
      a = str(a)
      e = "What is the perimeter of a regular octagon whose side lengths are "+a+"?"
      f = "Since this is a octagon, all eight sides have the same side length. We can multiply one side length, "+a+", by eight. 8 x "+a+" = "+d+"."
    if shape == "circle":
      d = str(a*a)+"π"
      a = str(a)
      e = "What is the circumference of a circle whose radius is "+a+", in terms of π?"
      f = "The circumference of a circle is twice its radius times π, or 2πr. Plugging this in, we get 2 x π x "+a+" = "+d+"."
    return d, e, f

  def area_problem():
    shapes = ["triangle", "square", "rectangle", "trapezoid", "circle"]
    shape = random.choice(shapes)
    if shape == "triangle":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      d = str(0.5*a*b)
      a = str(a)
      b = str(b)
      c = "What is the area of a triangle whose base is "+"a"+" and whose height is "+b+"?"
      e = "Since this is a triangle, we multiply the base times the height, then divide by 2, because base times height gives a rectangle double the size of the triangle. ("+a+" x "+b+")/2 = "+d+"."
    if shape == "square":
      a = random.randint(10, 99)
      d = str(a*a)
      a = str(a)
      c = "What is the area of a square whose side length is "+a+"?"
      e = "Since this is a square, the length and width are the same, and the area can be obtained by multiplying them. "+a+" x "+a+" = "+d+"."
    if shape == "rectangle":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      d = str(a*b)
      a = str(a)
      b = str(b)
      c = "What is the area of a rectangle whose side lengths are "+a+" and "+b+"?"
      e = "In a rectangle, the area can be obtained by multiplying the length and width. "+a+" x "+b+" = "+d+"."
    if shape == "trapezoid":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      h = random.randint(10, 99)
      d = str(((a+b)/2)*h)
      a = str(a)
      b = str(b)
      h = str(h)
      c = "What is the area of a trapezoid whose bases are "+a+" and "+b+", and whose height is "+h+"?"
      e = "The formula for the area of a trapezoid is the average of both bases times the height. (("+a+"+"+b+")/2) x "+h+" = "+d+"."
    if shape == "circle":
      a = random.randint(10, 99)
      d = str(a*a)+"π"
      a = str(a)
      c = "What is the area of a circle whose radius is "+d+", in terms of π?"
      e = "The formula for the area of a circle is the radius squared times π. "+a+text.supscr("2")+" x π = "+d+"."
    return c, d, e

  def volume_problem():
    solids = ["cone", "cylinder", "cube", "rectangula solid", "sphere", "rectangular pyramid"]
    solid = random.choice(solids)
    if solid == "cone":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      d = str((1/3)*(a*a)*(b))+"π"
      a = str(a)
      b = str(b)
      e = "What is the volume of a cone whose radius is "+a+" and whose height is "+b+", in terms of π?"
      f = "The formula for the volume of a cone is (1/3) x (r"+text.supscr("2")+") x h x π. Plugging in the values, we get (1/3) x ("+a+text.supscr("2")+") x "+b+" x π. In terms of π, this is "+d+"π."
    if solid == "cube":
      a = random.randint(1, 46)
      d = str(a**3)
      a = str(a)
      e = "What is the volume of a cube whose side length is "+a+"?"
      f = "Since all the dimensions of a cube are the same, and it is a uniform shape, we can simply cube the side length to obtain the volume. "+a++text.supscr("2")+" = "+d+"."
    if solid == "cylinder":
      a = random.randint(10, 99)
      b = random.randint(10, 99)
      d = str((a*a)*b)+"π"
      a = str(a)
      b = str(b)
      e = "What is the volume of a cylinder whose radius is "+a+" and whose height is "+b+", in terms of π?"
      f = "The volume of a cylinder can be found by multiplying its base times its height. Since the base is a circle, we can use its formula to find it out. Plugging in the values, we get ("+a+text.supscr("2")+" x π) x "+b+", which is equal to "+d+"."
    if solid == "rectangular solid":
      a = random.randint(1, 46)
      b = random.randint(1, 46)
      c = random.randint(1, 46)
      d = str(a*b*c)
      a = str(a)
      b = str(b)
      c = str(c)
      e = "What is the volume of a rectangular prism whose dimensions are "+a+", "+b+", and "+c+"?"
      f = "Since this is a uniform solid, we can find the volume by multiplying all of its dimensions."+a+" x "+b+" x "+c+" = "+d+"."
    if solid == "sphere":
      a = random.randint(1, 46)
      d = str((4/3)*(a**3))+"π"
      a = str(a)
      e = "What is the volume of a sphere whose radius is "+a+", in terms of π?"
      f = "The formula for the volume of a sphere is (4/3)(π)(r"+text.supscr("3")+"). Plugging these values in, we get (4/3)(π)("+a+text.supscr("3")+"), which is equal to "+d+"."
    if solid == "rectangular pyramid":
      l = random.randint(1, 31)
      w = random.randint(1, 31)
      h = random.randint(1, 31)
      d = str((1/3)*l*w*h)
      l = str(l)
      w = str(w)
      h = str(h)
      e = "What is the volume of a rectangular pyramid whose length and width is "+l+" and "+w+" and whose height is "+h+"?"
      f = "The formula for the volume of a rectangular pyramid is 1/3 times the length times the width times the height. Plugging it in, we have (1/3)("+l+")("+w+")("+h+"), which is equal to "+d+"."
    return d, e, f

  def fraction_problem():
    operations = ("add", "subtract", "multiply", "divide")
    operation = random.choice(operations)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    frac1 = a/b
    frac2 = c/d
    if operation == "add":
      ans = str(Fraction(frac1+frac2).limit_denominator())
      den = int((b*d)/(math.gcd(b, d)))
      co1 = int(den/b)
      co2 = int(den/d)
      num1 = str(int(co1*a))
      num2 = str(int(co2*c))
      a = str(a)
      b = str(b)
      c = str(c)
      d = str(d)
      den = str(den)
      co1 = str(co1)
      co2 = str(co2)
      ques = "What is the sum of "+a+"/"+b+" and "+c+"/"+d+"?"
      exp = "In order to add the fractions, we need to find the least common multiple of the denominators, which is "+den+". Next, we need to multiply both fractions into an equivalent fraction, such that both of them have the least common multiple as the denominator. This can be done by multiplying the first fraction by "+co1+"/"+co1+" and the second fraction by "+co2+"/"+co2+". Doing this, we get "+num1+"/"+den+" plus "+num2+"/"+den+", which equals "+ans+"."
    if operation == "subtract":
      if frac1 > frac2:
        ans = str(Fraction(frac1-frac2).limit_denominator())
        den = int((b*d)/(math.gcd(b, d)))
        co1 = int(den/b)
        co2 = int(den/d)
        num1 = str(int(co1*a))
        num2 = str(int(co2*c))
        a = str(a)
        b = str(b)
        c = str(c)
        d = str(d)
        den = str(den)
        co1 = str(co1)
        co2 = str(co2)
        ques = "What is "+a+"/"+b+" minus "+c+"/"+d+"?"
        exp = "In order to subtract the fractions, we need to find the least common multiple of the denominators, which is "+den+". Next, we need to multiply both fractions into an equivalent fraction, such that both of them have the least common multiple as the denominator. This can be done by multiplying the first fraction by "+co1+"/"+co1+" and the second fraction by "+co2+"/"+co2+". Doing this, we get "+num1+"/"+den+" minus "+num2+"/"+den+", which equals "+ans+"."
      if frac2 > frac1:
        ans = str(Fraction(frac2-frac1).limit_denominator())
        den = int((b*d)/(math.gcd(b, d)))
        co1 = int(den/b)
        co2 = int(den/d)
        num1 = str(int(co1*a))
        num2 = str(int(co2*c))
        a = str(a)
        b = str(b)
        c = str(c)
        d = str(d)
        den = str(den)
        co1 = str(co1)
        co2 = str(co2)
        ques = "What is "+c+"/"+d+" minus "+a+"/"+b+"?"
        exp = "In order to add the fractions, we need to find the least common multiple of the denominators, which is "+den+". Next, we need to multiply both fractions into an equivalent fraction, such that both of them have the least common multiple as the denominator. This can be done by multiplying the first fraction by "+co2+"/"+co2+" and the second fraction by "+co1+"/"+co1+". Doing this, we get "+num2+"/"+den+" minus "+num1+"/"+den+", which equals "+ans+"."
    if operation == "multiply":
      ans = str(Fraction(frac1*frac2).limit_denominator())
      num = str(a*c)
      den = str(b*d)
      a = str(a)
      b = str(b)
      c = str(c)
      d = str(d)
      ques = "What is the product of "+a+"/"+b+" and "+c+"/"+d+"?"
      exp = "When we multiply fractions, we multiply the numerators and the denominators to get the answer. Doing this, we get "+num+" for the numerator and "+den+" for the denominator, which is equal to the fraction of "+ans+"."
    if operation == "divide":
      ans = str(Fraction(frac1/frac2).limit_denominator())
      num = str(a*d)
      den = str(b*c)
      a = str(a)
      b = str(b)
      c = str(c)
      d = str(d)
      ques = "What is "+a+"/"+b+" divided by "+c+"/"+d+"?"
      exp = "When we divide fractions, we multiply the first fraction by the reciprocal of the second fraction. Doing this, we get "+num+" for the numerator and "+den+" for the denominator, which is equal to the fraction of "+ans+"."
    return ans, ques, exp

  def statistics_problem():
    types = ["mean", "median", "mode", "range", "MAD"]
    type = random.choice(types)
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    c = random.randint(1, 25)
    d = random.randint(1, 25)
    e = random.randint(1, 25)
    if type == "mean":
      dataset = [a, b, c, d, e]
      data_ques = ', '.join(map(str, dataset))
      data_exp = '+'.join(map(str, dataset))
      ans = str(round(((a+b+c+d+e)/5), 2))
      a = str(a)
      b = str(b)
      c = str(b)
      d = str(d)
      e = str(e)
      ans = ans.rstrip('0').rstrip('.') if '.' in ans else ans
      ques = "What is the mean of the data set ("+data_ques+"), to the nearest hundredth?"
      exp = "The mean of a data set is the same as the average of all the values. To find the average, we add up all the values, and divide by the total number of values. In this case, ("+data_exp+")/5 = "+ans+"."
    if type == "median":
      dataset = [a, b, c, d, e]
      dataorder = sorted(dataset)
      ans = str(dataorder[2])
      a = str(a)
      b = str(b)
      c = str(c)
      d = str(d)
      e = str(e)
      dataset = ', '.join(map(str, dataset))
      dataorder = ', '.join(map(str, dataorder))
      ques = "What is the median of the data set ("+dataset+")?"
      exp = "The median of a data set is the middle value when the values are ordered from least to greatest (If there are an even number of values, the median is the average of the 2 middle values). Ordering this list from least to greatest, we get ("+dataorder+"). We can then see the middle value is "+ans+"."
    if type == "mode":
      dataset = [a, b, c, d, a]
      dataset = sorted(dataset, key=lambda k: random.random())
      ans = str(mode(dataset))
      dataset = ', '.join(map(str, dataset))
      ques = "What is the mode of the data set ("+dataset+")?"
      exp = "The mode of a data set is the value that appears the most times. From this data set, we can see that "+ans+" appears the most times, so it is the mode."
    if type == "range":
      dataset = [a, b, c, d, e]
      dataorder = sorted(dataset)
      least = dataorder[0]
      greatest = dataorder[4]
      ans = str(greatest-least)
      a = str(a)
      b = str(b)
      c = str(c)
      d = str(d)
      e = str(e)
      dataset = ', '.join(map(str, dataset))
      dataorder = ', '.join(map(str, dataorder))
      least = str(least)
      greatest = str(greatest)
      ques = "What is the range of the data set ("+dataset+")?"
      exp = "The range of a data set is the difference between the greatest and smallest values. We can see the greatest value is "+greatest+" and the least value is "+least+". The difference between them is "+ans+"."
    if type == "MAD":
      dataset = [a, b, c, d, e]
      mean = round(((a+b+c+d+e)/5), 2)
      ans = round(((abs(a-mean)+abs(b-mean)+abs(c-mean)+abs(d-mean)+abs(e-mean))/5), 2)
      ans = str(ans)
      ans = ans.rstrip('0').rstrip('.') if '.' in ans else ans
      mean = str(mean)
      dataset = ', '.join(map(str, dataset))
      ques = "What is the mean average deviation of the data ("+dataset+"), rounded to the nearest hundredth?"
      exp = "The mean average deviation of a data set is the average distance each value is from the mean. First, we find the mean, which is "+mean+". Then, we average the distance each value is from the mean. The distance can be found by taking the absolute value of the difference between each value and the mean. Doing this, we obtain "+ans+" as our answer."
    return ans, ques, exp

  def surfarea_problem():
    solids = ["cube", "rectangular solid", "cylinder"]
    solid = random.choice(solids)
    if solid == "cube":
      a = random.randint(1, 40)
      ans = str(6*a*a)
      a = str(a)
      ques = "What is the surface area of a cube whose side length is "+a+"?"
      exp = "The surface of a cube is composed of 6 equal sized squares. If we find the area of one square and multiply it by six, we get the surface area of the entire cube. Squaring "+a+" to find the area of a single square, and multiplying by six, we get "+ans+"."
    if solid == "rectangular solid":
      a = random.randint(1, 40)
      b = random.randint(1, 40)
      c = random.randint(1, 40)
      ans = str((2*a*b)+(2*a*c)+(2*b*c))
      a = str(a)
      b = str(b)
      c = str(b)
      ques = "What is the surface area of a rectangular prism whose length, width, and height are "+a+", "+b+", and "+c+", respectively?"
      exp = "The surface of a rectangular prism is composed of 3 pairs of equally sized rectangles. If we find the area of each of the three distinct rectangles, multiply by 2 to compensate for the other one, and add them together, we get the surface area of the prism. Plugging it in, we get (2 x "+a+" x "+b+")+(2 x "+a+" x "+c+")+(2 x "+b+" x "+c+") = "+ans+"."
    if solid == "cylinder":
      r = random.randint(1, 40)
      h = random.randint(1, 40)
      ans = str((2*r*r)+(2*r*h))+"π"
      r = str(r)
      h = str(h)
      ques = "What is the surface area of a cylinder whose radius is "+r+" and whose height is "+h+", in terms of π?"
      exp = "The surface area of a cylinder is composed of two circles, as well as its side, which is simply the circumference of the circle times the height. The formula we can derive is 2r"+text.supscr("2")+"π+2πrh. Plugging it in, we get (2 x "+r+text.supscr("2")+" x π)+(2 x π x "+r+" x "+h+") = "+ans+"."
    return ans, ques, exp

  def variable1_problem():
    operations = ["add", "sub", "mul", "div"]
    operation = random.choice(operations)
    if operation == "add":
      a = random.randint(1, 75)
      b = random.randint(1, 150)
      ans = str(b-a)
      a = str(a)
      b = str(b)
      ques = "Given the equation x+"+a+" = "+b+", what is the value of x?"
      exp = "In order to solve for x, we need to isolate it. We can do this by subtracting "+a+" from both sides. Doing this, we get x = "+ans+"."
    if operation == "sub":
      a = random.randint(1, 75)
      b = random.randint(1, 75)
      ans = str(a+b)
      a = str(a)
      b = str(b)
      ques = "Given the equation x - "+a+" = "+b+", what is the value of x?"
      exp = "In order to solve for x, we need to isolate it. We can do this by adding "+a+" to both sides. Doing this, we get x = "+ans+"."
    if operation == "mul":
      a = random.randint(1, 50)
      ans = random.randint(1, 50)
      b = str(a*ans)
      a = str(a)
      ans = str(ans)
      ques = "Given the equation "+a+"x = "+b+", what is the value of x?"
      exp = "In order to solve for x, we need to isolate it. We can do this by dividing both sides by "+a+". Doing this, we get x = "+ans+"."
    if operation == "div":
      a = random.randint(1, 50)
      b = random.randint(1, 50)
      ans = str(a*b)
      a = str(a)
      b = str(b)
      ques = "Given the equation x/"+a+" = "+b+", what is the value of x?"
      exp = "In order to solve for x, we need to isolate it. We can do this by multiplying both sides by "+a+". Doing this, we get x = "+ans+"."
    return ans, ques, exp

  def variable2_problem():
    ans1 = ""
    ans2 = ""
    operations = ["+", "-"]
    a = random.randint(5, 10)
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    d = random.randint(6, 11)
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    sign1 = random.choice(operations)
    sign2 = random.choice(operations)
    if sign1 == "+":
      ans1 = (a*x)+(b*y)
    else:
      ans1 = (a*x)-(b*y)
    if sign2 == "+":
      ans2 = (c*x)+(d*y)
    else:
      ans2 = (c*x)-(d*y)
    co1 = a/c
    stu2 = d*co1
    stu3 = ans2*co1
    stu4 = b-stu2
    stu5 = ans1-stu3
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    ans1 = str(ans1)
    ans2 = str(ans2)
    x = str(x)
    y = str(y)
    stu2 = str(stu2)
    stu3 = str(stu3)
    co1 = str(co1)
    stu4 = str(stu4)
    stu5 = str(stu5)
    ans = "x = "+x+", y = "+y
    ques = "Given the equations "+a+"x+"+b+"y = "+ans1+" and "+c+"x+"+d+"y = "+ans2+", what does x and y equal? (Send answer in format x = ?, y = ?)"
    exp = "In order to solve for x and y, we must remove a variable to isolate the other. This can be done by multiplying one equation and subtracting it from the other. We will solve for y first. This can be done by multiplying the second equation by "+co1+". This gives us "+a+"x "+sign1+" "+stu2+"y = "+stu3+". Subtracting the second equation from the first, we get "+stu4+"y = "+stu5+". If we divide both sides by "+stu4+", we get y = "+y+". In order to solve for x, we can plug y back into any of the two equations. This gives us x = "+x+"."
    return ans, ques, exp

  def logrules_problem():
    rules = ["product", "quotient", "power"]
    rule = random.choice(rules)
    if rule == "product":
      a = random.randint(1, 31)
      b = random.randint(1, 31)
      ans = "log("+str(a*b)+")"
      a = str(a)
      b = str(b)
      ques = "Condense the logarithmic expression *log*("+a+")+*log*("+b+"). (Input answer as unsolved condensed logarithmic expression)"
      exp = "The product rule of logarithmic expressions states that *log*"+text.subscr("k")+"(a)+*log*"+text.subscr("k")+"(b) is equal to *log*"+text.subscr("k")+"(a x b). Since our expression is a sum, it is equal to the log of "+a+" x "+b+", which is equal to "+ans+"."
    if rule == "quotient":
      c = random.randint(1, 31)
      a = random.randint(1, 31)
      b = str(a*c)
      ans = "log("+str(c)+")"
      a = str(a)
      b = str(b)
      ques = "Condense the logarithmic expression *log*("+b+") - *log*("+a+"). (Input answer as unsolved condensed logarithmic expression)"
      exp = "The quotient rule of logarithmic expressions states that *log*"+text.subscr("k")+"(a) - *log*"+text.subscr("k")+"(b) is equal to *log*"+text.subscr("k")+"(a/b). Since our expression is a difference, it is equal to the log of "+b+"/"+a+", which is equal to "+ans+"."
    if rule == "power":
      a = random.randint(2, 9)
      a = str(a)
      ans = a+"log(x)"
      ques = "What is the expanded form of *log*(x"+text.supscr(str(a))+")? (Input answer as expanded unsolved logarithmic expression)"
      exp = "The power rule of logarithmic expressions states that *log*"+text.subscr("k")+"(a"+text.supscr("b")+") is equal to b*log*"+text.subscr("k")+"(a). Using this, we get "+ans+"."
    return ans, ques, exp

  def basictrig_problem():
    trigs = ["sine", "cosine", "tangent"]
    trig = random.choice(trigs)
    if trig == "sine":
      angle = random.randint(1, 360)
      radian = math.radians(angle)
      ans = str(round((math.sin(radian)), 2))
      angle = str(angle)
      ques = "What's the sine of "+angle+" degrees, rounded to the nearest hundredth?"
    if trig == "cosine":
      angle = random.randint(1, 360)
      radian = math.radians(angle)
      ans = str(round((math.cos(radian)), 2))
      angle = str(angle)
      ques = "What's the cosine of "+angle+" degrees, rounded to the nearest hundredth?"
    if trig == "tangent":
      angle1 = random.randint(1, 89)
      angle2 = random.randint(91, 269)
      angle3 = random.randint(271, 359)
      angle = random.choice([angle1, angle2, angle3])
      radian = math.radians(angle)
      ans = str(round((math.tan(radian)), 2))
      angle = str(angle)
      ques = "What's the tangent of "+angle+" degrees, rounded to the nearest hundredth?"
    return ans, ques

  def radtodeg_problem():
    options = ["rtod", "dtor"]
    option = random.choice(options)
    if option == "rtod":
      ans = random.randint(1, 720)
      radian = str(Fraction(ans/180).limit_denominator())+" π"
      ans = str(ans)
      ques = "What is "+radian+" radians as degrees?"
      exp = "In order to convert radians to degrees, we have to multiply it by 180/π. Doing this, we obtain "+ans+"."
    if option == "dtor":
      angle = random.randint(1, 720)
      ans = str(Fraction(angle/180).limit_denominator())+" π"
      angle = str(angle)
      ques = "What is "+angle+" degrees converted to radians, in terms of π? (Input answer as improper fraction space π)"
      exp = "In order to convert degrees to radians, we have to multiply it by π/180. Doing this and simplifying, we obtain "+ans+"."
    return ans, ques, exp

  def inequality_problem():
    a = ""
    b = ""
    pssign = ""
    exp_1 = ""
    sign_1 = ""
    coefficients = ["pp", "pn", "np", "nn"]
    coefficient = random.choice(coefficients)
    if coefficient == "pp":
      a = random.randint(1, 10)
      b = random.randint(1, 10)
      pssign = "+"
      exp_1 = ""
    elif coefficient == "pn":
      a = random.randint(1, 10)
      b = random.randint(-10, -1)
      pssign = "-"
      exp_1 = ""
    elif coefficient == "np":
      a = random.randint(-10, -1)
      b = random.randint(1, 10)
      pssign = "+"
      exp_1 = "Don't forget, since the coefficient is negative, we switch the sign around when dividing both sides."
    else:
      a = random.randint(-10, -1)
      b = random.randint(-10, -1)
      pssign = "-"
      exp_1 = "Don't forget, since the coefficient is negative, we switch the sign around when dividing both sides."
    b_1 = abs(b)
    signs = [">", "<"]
    sign = random.choice(signs)
    if a < 0:
      if sign == ">":
        sign_1 = "<"
      if sign == "<":
        sign_1 = ">"
    else:
      sign_1 = sign
    x = random.randint(1, 10)
    c = str((a*x)+b)
    ans = "x "+str(sign_1)+" "+str(x)
    ques = "Solve the inequality "+str(a)+"x "+str(pssign)+" "+str(b_1)+" "+str(sign)+" "+str(c)+" for x."
    exp = "The inequality can be solved by isolating x, which gives us "+str(ans)+". "+exp_1
    return ans, ques, exp

  def power_problem():
    operations = ["add", "sub", "mul"]
    operation = random.choice(operations)
    if operation == "add":
      a = random.randint(1, 10)
      b = random.randint(1, 10)
      c = a+b
      ans = "x^"+str(c)
      fans = "x"+text.supscr(str(c))
      ques = "What is the simplified form of the expression x"+text.supscr(str(a))+" * x"+text.supscr(str(b))+"? (Put answer as x^exponent)"
      exp = "If we are multiplying (a"+text.supscr("b")+")(a"+text.supscr("c")+"), it is equivalent to a"+text.supscr("b+c")+". Applying this, we add "+str(a)+" and "+str(b)+" to get "+str(c)+". This gives the answer of "+fans+"."
    if operation == "sub":
      b = random.randint(1, 10)
      c = random.randint(1, 10)
      a = b+c
      ans = "x^"+str(c)
      fans = "x"+text.supscr(str(c))
      ques = "What is the simplified form of the expression (x"+text.supscr(str(a))+")/(x"+text.supscr(str(b))+")? (Put answer as x^exponent)"
      exp = "If we are dividing (a"+text.supscr("b")+")/(a"+text.supscr("c")+"), it is equivalent to a"+text.supscr("b-c")+". Applying this, we get "+str(a)+" - "+str(b)+", which is equal to "+str(c)+". This gives us our answer, "+fans+"."
    if operation == "mul":
      a = random.randint(1, 10)
      b = random.randint(1, 10)
      c = a*b
      ans = "x^"+str(c)
      fans = "x"+text.supscr(str(c))
      ques = "What is the simplified form of the expression (x"+text.supscr(str(a))+")"+text.supscr(str(b))+"? (Put answer as x^(exponent))"
      exp = "If we have the expression (a"+text.supscr("b")+")"+text.supscr("c")+", it is equivalent to a"+text.supscr("b*c")+". Applying this, we get "+str(a)+" x "+str(b)+" is equal to "+str(c)+". This gives us our answer, "+fans+"."
    return ans, fans, ques, exp

  def rational_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    numb = [2, 3, 5, 6, 7, 8, 10]
    c = random.choice(numb)
    signs = ["+", " - "]
    sign = random.choice(signs)
    cons = ""
    if sign == "+":
      cons = " - "
    if sign == " - ":
      cons = "+"
    num = str(a*b)+cons+str(a)+"sqrt("+str(c)+")"
    fnum = str(a*b)+cons+str(a)+"√("+str(c)+")"
    den = str((b**2)-c)
    ans = num+"/"+den
    fans = fnum+"/"+den
    ques = "What is the rationalized form of the fraction "+str(a)+"/"+str(b)+sign+"√("+str(c)+")? (Do not simplify fraction)"
    exp = "In order to rationalize a fraction, we need to multiply both sides by the conjugate. Since the denominator is "+str(b)+sign+"√("+str(c)+"), the conjugate is "+str(b)+cons+"√("+str(c)+"). Multiplying this by both the numerator and denominator yields us the answer "+ans+"."
    return ans, fans, ques, exp

  def pold_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    dividend = str(a*c)+"x"+ text.supscr("3")+"+"+str((a*d)+(b*c))+"x"+text.supscr("2")+"+"+str((a*e)+(b*d))+"x+"
    divisor = str(a)+"x+"
    quotient = str(c)+"x^2+"+str(d)+"x+"
    fquotient = str(c)+"x"+text.supscr("2")+"+"+str(d)+"x+"
    dividend = dividend.replace(" 1x", " x")
    divisor = divisor.replace("1x", "x")
    quotient = quotient.replace(" 1x", " x")
    dividend = dividend+str(b*e)
    divisor = divisor+str(b)
    quotient = quotient+str(e)
    fquotient = fquotient+str(e)
    ques = "Divide "+dividend+" by "+divisor+" using polynomial long division."
    return quotient, fquotient, ques

  def pyt_problem():
    side_a = [3, 5, 8, 7, 20, 12, 9, 28, 11, 16, 33, 48, 13, 36, 39, 65]
    side_b = [4, 12, 15, 24, 21, 35, 40, 45, 60, 63, 56, 55, 84, 77, 80, 72]
    side_c = [5, 13, 17, 25, 29, 37, 41, 53, 61, 65, 65, 73, 85, 85, 89, 97]
    a = random.choice(side_a)
    ai = side_a.index(a)
    b = side_b[ai]
    c = side_c[ai]
    mults = [i for i in range(1, 19) if c*i < 100]
    mult = random.choice(mults)
    a = str(a*mult)
    b = str(b*mult)
    c = str(c*mult)
    answers = [a, b, c]
    ans = str(random.choice(answers))
    if ans == a:
      ques = "What is the remaining side length if the hypotenuse is "+c+" and the other side is "+b+"?"
    elif ans == b:
      ques = "What is the remaining side length if the hypotenuse is "+c+" and the other side is "+a+"?"
    else:
      ques = "What is the hypotenuse if the side lengths are "+a+" and "+b+"?"
    return ans, ques

  def triuni_problem():
    funcs = ["sin", "cos", "tan"]
    func = random.choice(funcs)
    angs = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
    ang = random.choice(angs)
    para = angs.index(ang)
    ang = str(ang)
    if func == "sin":
      anss = ["0", "1/2", "sqrt(2)/2", "sqrt(3)/2", "1", "sqrt(3)/2", "sqrt(2)/2", "1/2", "0", "-1/2", "-sqrt(2)/2", "-sqrt(3)/2", "-1", "-sqrt(3)/2", "-sqrt(2)/2", "-1/2"]
      ans = anss[para]
      fanss = ["0", "1/2", "√(2)/2", "√(3)/2", "1", "√(3)/2", "√(2)/2", "1/2", "0", "-1/2", "-√(2)/2", "-√(3)/2", "-1", "-√(3)/2", "-√(2)/2", "-1/2"]
      fans = fanss[para]
    if func == "cos":
      anss = ["1", "sqrt(3)/2", "sqrt(2)/2", "1/2", "0", "-1/2", "-sqrt(2)/2", "-sqrt(3)/2", "-1", "-sqrt(3)/2", "-sqrt(2)/2", "-1/2", "0", "1/2", "sqrt(2)/2", "sqrt(3)/2"]
      ans = anss[para]
      fanss = ["1", "√(3)/2", "√(2)/2", "1/2", "0", "-1/2", "-√(2)/2", "-√(3)/2", "-1", "-√(3)/2", "-√(2)/2", "-1/2", "0", "1/2", "√(2)/2", "√(3)/2"]
      fans = fanss[para]
    if func == "tan":
      anss = ["0", "sqrt(3)/3", "1", "sqrt(3)", "Undefined", "-sqrt(3)", "-1", "-sqrt(3)/3", "0", "sqrt(3)/3", "1", "sqrt(3)", "Undefined", "-sqrt(3)", "-1", "-sqrt(3)/3"]
      ans = anss[para]
      fanss = ["0", "√(3)/3", "1", "√(3)", "Undefined", "-√(3)", "-1", "-√(3)/3", "0", "√(3)/3", "1", "√(3)", "Undefined", "-√(3)", "-1", "-√(3)/3"]
      fans = fanss[para]
    ques = "What is "+func+"("+ang+"), using the unit circle? (Angle is in degrees, rationalize the denominator, and type in Undefined if answer is undefined)"
    return ans, fans, ques

  def compsq_problem():
    b = 2*random.randint(-5, 5)
    c = random.randint(1, 20)
    ques "Solve for the roots of the equation x"+text.supscr("2")+" + "+str(b)+"x + "+str(c)+" = 0 by completing the square. (± sign)"
    interb = b/2
    interbb = interb**2
    ans = str(-1*interb)+" ± √("+str(interbb-c)+")"
    fans = str(-1*interb)+" ± sqrt("+str(interbb-c)+")"
    exp = "To complete the square, we first subtract "+str(c)+" from both sides, to make it x"+text.supscr("2")+" + "+str(b)+"x = "+str(c*-1)+". Then, in order to make the left hand side a perfect square, we add "+str(interbb)+" to both sides, which allows us to factor the left hand side and end up with (x + "+str(interb)+")"+text.supscr("2")+" = "+str(interbb-c)+". Further simplifying and solving for x yields "+ans+"."
    return ans, fans, ques, exp
    
