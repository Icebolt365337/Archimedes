from generate import generate
import discord
import os
import requests
client = discord.Client()
import aiohttp

list_of_topics = '''
    List of Topics - Type corresponding command to get subtopics
    1. Operations - !op
    2. Algebraic Equations and Inequalities - !alg
    3. Functions - !fun
    4. Geometry - !geo
    5. Quadratics - !quadratics
    6. Complex Numbers - !complx
    7. Probability & Statistics - !pstat
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
    2. Exponential and Logarithmic Functions - !explogfun
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

@client.event
async def on_ready():
    print("Time to test!")

res = None
exp = None
fres = None
na = "There are no explanations for this subtopic."

@client.event
async def on_message(message):
    global res
    global exp
    global fres
    if message.author == client.user:
        return
    if (res or fres):
        if (message.content.replace(" ", "")).startswith(res or fres):
            embed = text.embed("", "That's Correct!")
            user.send(user, embed=embed)
        else:
          if (fres):
            await message.channel.send("The correct answer is " + fres + ".")
          else:
            await message.channel.send("The correct answer is " + res + ".")
        res = None
        fres = None
    if message.content.startswith('!'):
        if message.content.startswith('!exp'):
          if exp != None:
            await message.channel.send(exp)
            exp = None
          else:
            await message.channel.send("There is no question for which you are requesting an explanation. Please ask for a question first. You can find topics by sending !help.")
        elif message.content.startswith('!help'):
            await message.channel.send(
              list_of_topics)
        elif message.content.startswith('!op'):
            await message.channel.send(list_of_operations)
        elif message.content.startswith('!alg'):
            await message.channel.send(list_of_algebra)
        elif message.content.startswith('!fun'):
            await message.channel.send(list_of_functions)
        elif message.content.startswith('!geo'):
            await message.channel.send(list_of_geometry)
        elif message.content.startswith('!quadratics'):
            await message.channel.send(list_of_quadratics)
        elif message.content.startswith('!complx'):
            await message.channel.send(list_of_complex_numbers)
        elif message.content.startswith('!pstat'):
            await message.channel.send(list_of_probability_statistics)
        elif message.content.startswith('!basop'):
            ques, res = generate.basicop_problem()
            await message.channel.send(ques)
            exp = na
        elif message.content.startswith('!per'):
            res, ques, exp = generate.perimeter_problem()
            await message.channel.send(ques)
        elif message.content.startswith('!area'):
            ques, res, exp = generate.area_problem()
            await message.channel.send(ques)
        elif message.content.startswith('!neg'):
            res, ques = generate.negative_problem()
            await message.channel.send(ques)
            exp = na
        elif message.content.startswith('!vol'):
          res, ques, exp = generate.volume_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!frac'):
          res, ques, exp = generate.fraction_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!data'):
          res, ques, exp = generate.statistics_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!sa'):
          res, ques, exp = generate.surfarea_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!var1'):
          res, ques, exp = generate.variable1_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!var2'):
          res, ques, exp = generate.variable2_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!logr'):
          res, ques, exp = generate.logrules_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!btrig'):
          res, ques = generate.basictrig_problem()
          await message.channel.send(ques)
          exp = na
        elif message.content.startswith('!rtod'):
          res, ques, exp = generate.radtodeg_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!ineq'):
          res, ques, exp = generate.inequality_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!powr'):
          res, fres, ques, exp = generate.power_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!rat'):
          res, fres, ques, exp = generate.rational_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!pold'):
          res, fres, ques = generate.pold_problem()
          await message.channel.send(ques)
          exp = na
        elif message.content.startswith('!pyt'):
          res, ques = generate.pyt_problem()
          await message.channel.send(ques)
          exp = na
        elif message.content.startswith('!triuni'):
          res, fres, ques = generate.triuni_problem()
          await message.channel.send(ques)
          exp = na
        elif message.content.startswith('!compsq'):
          res, fres, ques, exp = generate.compsq_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!fac'):
          res, fres, ques, exp = generate.factoring_problem()
          await message.channel.send(ques)
        elif message.content.startswith('!quadform'):
          res, fres, ques, exp = generate.quadform_problem()
          await message.channel.send(ques)
        else:
          await message.channel.send("This is not a valid command. If in the help section, this command is most likely not available yet.");

client.run(os.environ.get('TOKEN'))
