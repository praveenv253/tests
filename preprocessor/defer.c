#define EMPTY
#define DEFER(id) id EMPTY
#define OBSTRUCT(id) id DEFER(EMPTY)()
#define EXPAND(...) __VA_ARGS__

#define A() 123
// Expands to 123
A()
// Expands to A () because it requires one more scan to fully expand
DEFER(A)()
// Expands to 123, because the EXPAND macro forces another scan
EXPAND(DEFER(A)())
