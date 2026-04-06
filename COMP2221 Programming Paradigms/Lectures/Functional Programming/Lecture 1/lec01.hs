-- Use module load haskell/9.6.2

-- Load standard library "Prelude" (loaded by default)
import Prelude

-- Naming rules:
-- Identifiers, e.g. variable and function names, consist of letters, numbers, _ (underscore) and ' (prime)
-- Variables and functions must start with a lower case letter or underscore
-- Types must start with an upper case letter

-- declare variables
-- can add type annotations for improved readability
x :: Int
x = 3

-- variables in Haskell are immutable - they are defined once and cannot change
-- x = 5

-- unary function
id' :: Int -> Int
id' x = x

-- binary function
f :: Int -> Int -> Int
f x y = x + 2*y

-- define lists
xs :: [Int]
xs = [11,22,33,44]

xss :: [[Int]]
xss = [[111,222],[333,444]]

ys :: [Int]
ys = [11,22,33,44,55,66]

-- Entry point of a Haskell program is called "main"
-- Specifies a sequence of events via do syntax
main :: IO ()
main =
  do

  -- hello world
  print "Hello World"

  -- function composition
  print (f 3 5)
  print (f (id' 3) (id' 5))
  
  -- prefix to infix
  print (3 `f` 5)
  
  -- infix to prefix      
  print ((+) 3 8)
  
  -- list operations

  -- head
  print(head ys)
  
  -- tail
  print(tail ys)
  

  
  -- init
  print(init ys)
  
  -- last
  print(last ys)
  
  -- length
  print(length ys)
        
  -- take 3 
  print (take 3 ys)