#include <atomic>

using namespace std;

struct spin_lock
{
    atomic<bool> lock;

    void lock()
};

