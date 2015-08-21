mytake :: Int -> [Int] -> [Int]
mytake 1 l = head l : []
mytake n l = head l : mytake (n-1) (tail l)
	{-Error when trying to take more elements than the list contains-}
