from generate import generate
import discord
import os
import requests
client = discord.Client()
import aiohttp
from text import text

list_of_topics = '''
    List of Topics - Type corresponding command to get subtopics
    1. Operations - !operations
    2. Algebraic Equations and Inequalities - !algebra
    3. Functions - !functions
    4. Geometry - !geometry
    5. Quadratics - !quadratics
    6. Complex Numbers - !complex
    7. Probability & Statistics - !probability
    8. Explanation - !exp (Select subtopics don't provide explanations)
    '''

list_of_operations = '''
    List of Operation Subtopics - Type corresponding command to get problems
    1. Basic Operations - !basop
    2. Negative Numbers - !neg
    3. Fractions - !frac
    '''

list_of_algebra = '''
    List of Algebraic Equations and Inequalities Subtopics - Type corresponding command to get problems
    1. Equations: One Variable - !var1
    2. Equations: Two Variables - !var2
    3. Solving Inequalities - !ineq
    4. Power Rules - !powr
    5. Rationalizing Fractions - !rat
    6. Polynomial Long Division - !pold
    7. Logarithmic Rules - !logr
    '''

list_of_functions = '''
    List of Function Subtopics - Type corresponding command to get problems
    1. Function Composition - !funcomp
    2. Exponential and Logarithmic Functions - !logexpfun
    3. Trigonometric Functions - !trigfun
    '''

list_of_geometry = '''
    List of Geometry Subtopics - Type corresponding command to get problems
    1. Perimeter - !per
    2. Area - !area
    3. Surface Area - !sa
    4. Volume - !vol
    5. Pythagorean's Theorem - !pyt
    6. Radians and Degrees Conversion - !rtod
    7. Basic Trigonometry - !btrig
    8. Trigonometry: Unit Circle - !triuni
    '''

list_of_quadratics = '''
    List of Quadratics Subtopics - Type corresponding command to get problems
    1. Quadratic Equations: Completing the Square - !compsq
    2. Quadratic Equations: Factoring - !fac
    3. Quadratic Equations: Quadratic Formula - !quafor
    '''

list_of_complex_numbers = '''
    List of Complex Number Subtopics - Type corresponding command to get problems
    1. Complex Number Conjugates - !comcon
    2. Complex Number Roots - !comroot
    '''

list_of_probability_statistics = '''
    List of Probability and Statistics Subtopics - Type corresponding command to get problems
    1. Mean, Median, Mode, Range, MAD - !data
    2. Probability: Addition - !padd
    3. Probability: Multiplication - !pmult
    '''

res = None
exp = None
fres = None
embed = None
na = "There are no explanations for this subtopic."

@client.event
async def on_message(message):
    global res
    global exp
    global fres
    global embed
    if message.author == client.user:
        return
    if (res or fres):
        if message.content.replace(' ', '').startswith(res) or message.content.replace(' ', '').startswith(fres):
            embed = text.embed("", "That's Correct!")
            await message.channel.send(embed=embed)
        else:
          if (res):
            embed = text.embed("", "The correct answer is " + res + ".")
            await message.channel.send(embed=embed)
          else:
            embed = text.embed("", "The correct answer is " + fres + ".")
            await message.channel.send(embed=embed)
        res = None
        fres = None
    if message.content.startswith('!'):
        if message.content.startswith('!exp'):
          if exp != None:
            embed = text.embed("", exp)
            await message.channel.send(embed=embed)
            exp = None
          else:
            embed = text.embed("", "There is no question for which you are requesting an explanation. Please ask for a question first. You can find topics by sending !help.")
            await message.channel.send(embed=embed)
        elif message.content.startswith('!help'):
            embed = text.embed("List Of Topics", list_of_topics)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!operations'):
            embed = text.embed("", list_of_operations)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!algebra'):
            embed = text.embed("", list_of_algebra)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!functions'):
            embed = text.embed("", list_of_functions)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!geometry'):
            embed = text.embed("", list_of_geometry)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!quadratics'):
            embed = text.embed("", list_of_quadratics)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!complex'):
            embed = text.embed("", list_of_complex_numbers)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!probability'):
            embed = text.embed("", list_of_probability_statistics)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!basop'):
            ques, res = generate.basicop_problem()
            embed = text.embed("", ques)
            await message.channel.send(embed=embed)
            exp = na
        elif message.content.startswith('!per'):
            res, ques, exp = generate.perimeter_problem()
            embed = text.embed("", ques)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!area'):
            ques, res, exp = generate.area_problem()
            embed = text.embed("", ques)
            await message.channel.send(embed=embed)
        elif message.content.startswith('!neg'):
            res, ques = generate.negative_problem()
            embed = text.embed("", ques)
            await message.channel.send(embed=embed)
            exp = na
        elif message.content.startswith('!vol'):
          res, ques, exp = generate.volume_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!frac'):
          res, ques, exp = generate.fraction_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!data'):
          res, ques, exp = generate.statistics_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!sa'):
          res, ques, exp = generate.surfarea_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!var1'):
          res, ques, exp = generate.variable1_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!var2'):
          res, ques, exp = generate.variable2_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!logr'):
          res, ques, exp = generate.logrules_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!btrig'):
          res, ques = generate.basictrig_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
          exp = na
        elif message.content.startswith('!rtod'):
          res, ques, exp = generate.radtodeg_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!ineq'):
          res, ques, exp = generate.inequality_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!powr'):
          res, fres, ques, exp = generate.power_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!rat'):
          res, fres, ques, exp = generate.rational_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!pold'):
          res, fres, ques = generate.pold_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
          exp = na
        elif message.content.startswith('!pyt'):
          res, ques = generate.pyt_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
          exp = na
        elif message.content.startswith('!triuni'):
          res, fres, ques = generate.triuni_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
          exp = na
        elif message.content.startswith('!compsq'):
          res, fres, ques, exp = generate.compsq_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!fac'):
          res, fres, ques, exp = generate.factoring_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        elif message.content.startswith('!quadform'):
          res, fres, ques, exp = generate.quadform_problem()
          embed = text.embed("", ques)
          await message.channel.send(embed=embed)
        else:
          embed = text.embed("", "This is not a valid command. If in the help section, this command is most likely not available yet.")
          await message.channel.send(embed=embed)

client.run(os.environ.get('TOKEN'))
