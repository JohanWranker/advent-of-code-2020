package advent.of.code

class App {
    static void main(String[] args) {
        println new File("../input").readLines().count { line ->
            def ( _, low, high, c, data) = ( line =~ /(\d+)-(\d+)\s+(\w):\s+(\w+)/)[0]
            def count = (data =~ /$c/).size()
            return low.toInteger() <= count && count <= high.toInteger()
        }

        println new File("../input").readLines().count { line ->
            def ( _, pos1, pos2, c, data) = ( line =~ /(\d+)-(\d+)\s+(\w):\s+(\w+)/)[0]
            return (data[pos1.toInteger()-1] == c) != (data[pos2.toInteger()-1] == c) 
        }
    }
}
