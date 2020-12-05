package advent.of.code


class Day03 {

    static int test(Integer x,Integer y) {
        def match = 0
        //println(System.getProperty("user.dir"))
        def a =  new File("input").readLines().eachWithIndex  { line, index ->
//            println ("Line ${line} ## ${index}")
            def length = line.size()
            def pos = (x*index) % line.size()
            def isX = line[pos] == "#"
            println ("Line ${line} %% ${index} %% length ${length} %% pos ${pos} %% X ${isX}")
            if (index % y == 0) {
                def trueIndex = (index/y).toInteger()
                if ( line[(x*trueIndex) % line.size()] == "#" ) {
                    match += 1
                }
            }
            return isX
        }

        println(match)
        return match
    }

    static void main(String[] args) {
        BigInteger f = 1
        f = f *test(1,1)
        f = f *test(3,1)
        f = f *test(5,1)
        f = f *test(7,1)
        f = f *test(1,2)
        println (f)
    }
}
