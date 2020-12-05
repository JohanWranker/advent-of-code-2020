package advent.of.code


class Day03 {

    static int test(def data, Integer x,Integer y) {
        return data.withIndex(0).count { line, index ->
            return index % y == 0 &&
                    line[(x * (index / y).toInteger()) % line.size()] == "#"
        }
    }

    static void main(String[] args) {
        def data = new File("input").readLines()
        BigInteger f = 1
        f = f *test(data, 1,1)
        f = f *test(data, 3,1)
        f = f *test(data, 5,1)
        f = f *test(data, 7,1)
        f = f *test(data, 1,2)
        println (f)
    }
}
