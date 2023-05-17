{- Let there be k different types of weather, where we denote each type of weather by a positive integer. For example, sunny = 0, rainy = 1, ..., cloudy = k.
Task

Find the probability of having weather j in n days from now given weather i today and conditional on some daily weather transition probabilities, a k*k matrix, where i and j are integers less than or equal to k.
Example

There are two types of weather 0 and 1. Transition probabilities:

[[0.6, 0.4],
 [0.3, 0.7]]

    The probability of weather 0 tomorrow if weather 0 today: 60%
    The probability of weather 1 tomorrow if weather 0 today: 40%
    The probability of weather 0 tomorrow if weather 1 today: 30%
    The probability of weather 1 tomorrow if weather 1 today: 70%

The probability of weather 0 two days from now if we start in weather 0 becomes: 60% * 60% + 40% * 30% = 48%. Because either we stay in 0 for two days or we go from 0 to 1 and then from 1 to 0.
Note

We will have k ≤ 10 and n ≤ 50.
 -}



module WeatherPrediction (weatherPrediction) where

import Data.List (transpose)

type Weather = Int
type Probability = Double

weatherPrediction :: Int -> Weather -> Weather -> [[Probability]] -> Probability
weatherPrediction 0 today final _ = if today == final then 1 else 0
weatherPrediction n today final pss = (pss `matrixPower` n) !! today !! final

matrixPower :: [[Probability]] -> Int -> [[Probability]]
matrixPower m 0 = identityMatrix (length m)
matrixPower m n
  | n > 0 = multiplyMatrices m (matrixPower m (n - 1))
  | otherwise = error "Negative exponent"

multiplyMatrices :: [[Probability]] -> [[Probability]] -> [[Probability]]
multiplyMatrices m1 m2 = [[sum $ zipWith (*) row col | col <- transpose m2] | row <- m1]

identityMatrix :: Int -> [[Probability]]
identityMatrix n = [[if i == j then 1 else 0 | j <- [0..n-1]] | i <- [0..n-1]]
