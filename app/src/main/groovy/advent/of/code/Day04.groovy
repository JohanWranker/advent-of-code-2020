package advent.of.code


class Day04 {
    static void main(String[] args) {
        int preamble = 5
        def data = new File("input").collect {it.toBigInteger()}

        def table = data.indexed().collect { it ->
            def low = it.key-preamble > 0 ? it.key-preamble : 0
            def high = it.key-1 > 0 ? it.key-1 : 0
            return data[low .. high]*.add(it.value)
        }
        print table
        def a = data.indexed().find { key, value ->
            return (key > preamble) && !table[key-preamble .. key-1].any {
                return value in it
            }
        }
        println("code ${a}")
    }
}
