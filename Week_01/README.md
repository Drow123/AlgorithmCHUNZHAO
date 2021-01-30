学习笔记
1. python xrange()函数
xrange()函数用法与range()完全相同，所不同的是生成的不是一个数组，而是一个生成器。
python3 取消了 xrange() 函数，并且和 range() 函数合并为 range()。
当调用 xrange() 的时候，python3 环境提示 xrange 没有被定义。

2. Java queue
Java queue遵循FIFO顺序来插入和删除它的元素；
最常用的queue实现是LinkedList，ArrayBlockingQueue 和PriorityQueue；

boolean add(E e)： 如果可以在不违反容量限制的情况下立即执行此操作，则将指定的元素插入此队列，成功时返回true，如果当前没有可用空间则抛出IllegalStateException。

boolean offer(E e)： 如果可以在不违反容量限制的情况下立即执行此操作，则将指定的元素插入此队列，成功时返回true，如果当前没有可用空间则返回 false。

E remove()：检索并删除此队列的头部元素。 此方法与poll的不同之处仅在于，如果此队列为空，则抛出异常 NoSuchElementException。

E poll()： 检索并删除此队列的头部，如果此队列为空，则返回null。

E element()：检索但不删除此队列的头部。 此方法与peek的不同之处仅在于，如果此队列为空，则抛出异常 NoSuchElementException。

E peek()：检索但不移除此队列的头部，如果此队列为空，则返回null。


3. Java PriorityQueue源码  参考链接：https://blog.csdn.net/qq_41907991/article/details/95666271?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161200315416780261976247%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161200315416780261976247&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-95666271.pc_search_result_no_baidu_js&utm_term=java+Queue+和+Priority+Queue+源码分析&spm=1018.2226.3001.4187
PriorityQueue是Queue的一个继承者，相比于一般的列表，它的特点是出队的时候可以按照优先级进行出队，所以不像LinkedList那样只能按照插入的顺序出队，PriorityQueue是可以根据给定的优先级顺序进行出队的。这里说的给定优先级顺序既可以是内部比较器，也可以是外部比较器。PriorityQueue内部是根据小顶堆的结构进行存储的，所谓小顶堆的意思，便是最小的元素总是在最上面，每次出队总是将堆顶元素移除，这样便能让出队变得有序。
    

内部成员：内部使用的是一个Object数组进行元素的存储。

    // 默认初始化容量
    private static final int DEFAULT_INITIAL_CAPACITY = 11;

    /**
     * 优先级队列是使用平衡二叉堆表示的: 节点queue[n]的两个孩子分别为
     * queue[2*n+1] 和 queue[2*(n+1)].  队列的优先级是由比较器或者
     * 元素的自然排序决定的， 对于堆中的任意元素n，其后代d满足：n<=d
     * 如果堆是非空的，则堆中最小值为queue[0]。
     */
    transient Object[] queue;

    /**
     * 队列中元素个数
     */
    private int size = 0;

    /**
     * 比较器
     */
    private final Comparator<? super E> comparator;

    /**
     * 修改次数
     */
    transient int modCount = 0;


构造函数，6个构造函数

    /**
     * 使用默认的容量（11）来构造一个空的优先级队列，使用元素的自然顺序进行排序（此时元素必须实现comparable接口）
     */
    public PriorityQueue() {
        this(DEFAULT_INITIAL_CAPACITY, null);
    }

    /**
     * 使用指定容量来构造一个空的优先级队列，使用元素的自然顺序进行排序（此时元素必须实现comparable接口）
     * 但如果指定的容量小于1则会抛出异常
     */
    public PriorityQueue(int initialCapacity) {
        this(initialCapacity, null);
    }

    /**
     * 使用默认的容量（11）构造一个优先级队列，使用指定的比较器进行排序
     */
    public PriorityQueue(Comparator<? super E> comparator) {
        this(DEFAULT_INITIAL_CAPACITY, comparator);
    }

    /**
     * 使用指定容量创建一个优先级队列，并使用指定比较器进行排序。
     * 但如果指定的容量小于1则会抛出异常
     */
    public PriorityQueue(int initialCapacity,
                         Comparator<? super E> comparator) {
        if (initialCapacity < 1)
            throw new IllegalArgumentException();
        this.queue = new Object[initialCapacity];
        this.comparator = comparator;
    }

    /**
     * 使用指定集合的所有元素构造一个优先级队列，
     * 如果该集合为SortedSet或者PriorityQueue类型，则会使用相同的顺序进行排序，
     * 否则，将使用元素的自然排序（此时元素必须实现comparable接口），否则会抛出异常
     * 并且集合中不能有null元素，否则会抛出异常
     */
    @SuppressWarnings("unchecked")
    public PriorityQueue(Collection<? extends E> c) {
        if (c instanceof SortedSet<?>) {
            SortedSet<? extends E> ss = (SortedSet<? extends E>) c;
            this.comparator = (Comparator<? super E>) ss.comparator();
            initElementsFromCollection(ss);
        }
        else if (c instanceof PriorityQueue<?>) {
            PriorityQueue<? extends E> pq = (PriorityQueue<? extends E>) c;
            this.comparator = (Comparator<? super E>) pq.comparator();
            initFromPriorityQueue(pq);
        }
        else {
            this.comparator = null;
            initFromCollection(c);
        }
    }

    /**
     * 使用指定的优先级队列中所有元素来构造一个新的优先级队列.  将使用原有顺序进行排序。
     */
    @SuppressWarnings("unchecked")
    public PriorityQueue(PriorityQueue<? extends E> c) {
        this.comparator = (Comparator<? super E>) c.comparator();
        initFromPriorityQueue(c);
    }

    /**
     * 根据指定的有序集合创建一个优先级队列，将使用原有顺序进行排序
     */
    @SuppressWarnings("unchecked")
    public PriorityQueue(SortedSet<? extends E> c) {
        this.comparator = (Comparator<? super E>) c.comparator();
        initElementsFromCollection(c);
    }


从集合中构造优先级队列的时候，调用了几个初始化函数
    private void initFromPriorityQueue(PriorityQueue<? extends E> c) {
        if (c.getClass() == PriorityQueue.class) {
            this.queue = c.toArray();
            this.size = c.size();
        } else {
            initFromCollection(c);
        }
    }

    private void initElementsFromCollection(Collection<? extends E> c) {
        Object[] a = c.toArray();
        // If c.toArray incorrectly doesn't return Object[], copy it.
        if (a.getClass() != Object[].class)
            a = Arrays.copyOf(a, a.length, Object[].class);
        int len = a.length;
        if (len == 1 || this.comparator != null)
            for (int i = 0; i < len; i++)
                if (a[i] == null)
                    throw new NullPointerException();
        this.queue = a;
        this.size = a.length;
    }

    private void initFromCollection(Collection<? extends E> c) {
        initElementsFromCollection(c);
        heapify();
    }
initFromPriorityQueue即从另外一个优先级队列构造一个新的优先级队列，此时内部的数组元素不需要进行调整，只需要将原数组元素都复制过来即可。但是从其他非PriorityQueue的集合中构造优先级队列时，需要先将元素复制过来后再进行调整，此时调用的是heapify方法：


  private void heapify() {
        // 从最后一个非叶子节点开始从下往上调整
        for (int i = (size >>> 1) - 1; i >= 0; i--)
            siftDown(i, (E) queue[i]);
    }

    // 划重点了，这个函数即对应上面的元素删除时从上往下调整的步骤
    private void siftDown(int k, E x) {
        if (comparator != null)
            // 如果比较器不为null，则使用比较器进行比较
            siftDownUsingComparator(k, x);
        else
            // 否则使用元素的compareTo方法进行比较
            siftDownComparable(k, x);
    }

    private void siftDownUsingComparator(int k, E x) {
        // 使用half记录队列size的一半，如果比half小的话，说明不是叶子节点
        // 因为最后一个节点的序号为size - 1，其父节点的序号为(size - 2) / 2或者(size - 3 ) / 2
        // 所以half所在位置刚好是第一个叶子节点
        int half = size >>> 1;
        while (k < half) {
            // 如果不是叶子节点，找出其孩子中较小的那个并用其替换
            int child = (k << 1) + 1;
            Object c = queue[child];
            int right = child + 1;
            if (right < size &&
                comparator.compare((E) c, (E) queue[right]) > 0)
                c = queue[child = right];
            if (comparator.compare(x, (E) c) <= 0)
                break;
            // 用c替换
            queue[k] = c;
            k = child;
        }
        // 
        queue[k] = x;
    }
    // 同上，只是比较的时候使用的是元素的compareTo方法
    private void siftDownComparable(int k, E x) {
        Comparable<? super E> key = (Comparable<? super E>)x;
        int half = size >>> 1;        // 如果是非叶子节点则继续循环
        while (k < half) {
            int child = (k << 1) + 1;
            Object c = queue[child];
            int right = child + 1;
            if (right < size &&
                ((Comparable<? super E>) c).compareTo((E) queue[right]) > 0)
                c = queue[child = right];
            if (key.compareTo((E) c) <= 0)
                break;
            queue[k] = c;
            k = child;
        }
        queue[k] = key;
    }

//siftUp()函数
 private void siftUp(int k, E x) {
        if (comparator != null)
            siftUpUsingComparator(k, x);
        else
            siftUpComparable(k, x);
    }

    @SuppressWarnings("unchecked")
    private void siftUpComparable(int k, E x) {
        Comparable<? super E> key = (Comparable<? super E>) x;
        while (k > 0) {
            int parent = (k - 1) >>> 1;
            Object e = queue[parent];
            if (key.compareTo((E) e) >= 0)
                break;
            queue[k] = e;
            k = parent;
        }
        queue[k] = key;
    }

    @SuppressWarnings("unchecked")
    private void siftUpUsingComparator(int k, E x) {
        while (k > 0) {
            int parent = (k - 1) >>> 1;
            Object e = queue[parent];
            if (comparator.compare(x, (E) e) >= 0)
                break;
            queue[k] = e;
            k = parent;
        }
        queue[k] = x;
    }


常用方法：add、offer、grow(扩容)、poll等。

public boolean add(E e) {
        return offer(e);
    }

    public boolean offer(E e) {
        if (e == null)
            throw new NullPointerException();
        modCount++;
        int i = size;
        if (i >= queue.length)
            grow(i + 1);
        size = i + 1;
        if (i == 0)
            queue[0] = e;
        else
            siftUp(i, e);
        return true;
    }
    // 扩容函数
    private void grow(int minCapacity) {
        int oldCapacity = queue.length;
        // 如果当前容量比较小（小于64）的话进行双倍扩容，否则扩容50%
        int newCapacity = oldCapacity + ((oldCapacity < 64) ?
                                         (oldCapacity + 2) :
                                         (oldCapacity >> 1));
        // 如果发现扩容后溢出了，则进行调整
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        queue = Arrays.copyOf(queue, newCapacity);
    }
    private static int hugeCapacity(int minCapacity) {
        if (minCapacity < 0) // overflow
            throw new OutOfMemoryError();
        return (minCapacity > MAX_ARRAY_SIZE) ?
            Integer.MAX_VALUE :
            MAX_ARRAY_SIZE;
    }

    public boolean contains(Object o) {
        return indexOf(o) != -1;
    }

    private int indexOf(Object o) {
        if (o != null) {
            // 查找时需要进行全局遍历，比搜索二叉树的查找效率要低
            for (int i = 0; i < size; i++)
                if (o.equals(queue[i]))
                    return i;
        }
        return -1;
    }

    public E poll() {
        if (size == 0)
            return null;
        int s = --size;
        modCount++;
        E result = (E) queue[0];
        E x = (E) queue[s];
        queue[s] = null;
        if (s != 0)
            siftDown(0, x);
        return result;
    }
 
remove方法

  // 这里不是移除堆顶元素，而是移除指定元素
    public boolean remove(Object o) {
        // 先找到该元素的位置
        int i = indexOf(o);
        if (i == -1)
            return false;
        else {
            removeAt(i);
            return true;
        }
    }
    // 移除指定序号的元素
    private E removeAt(int i) {
        // assert i >= 0 && i < size;
        modCount++;
        // s为最后一个元素的序号
        int s = --size;
        if (s == i)
            queue[i] = null;
        else {
            // moved记录最后一个元素的值
            E moved = (E) queue[s];
            queue[s] = null;
            // 用最后一个元素代替要移除的元素，并向下进行调整
            siftDown(i, moved);
            // 如果向下调整后发现moved还在该位置，则再向上进行调整
            if (queue[i] == moved) {
                siftUp(i, moved);
                if (queue[i] != moved)
                    return moved;
            }
        }
        return null;
    }

4. 双指针类题目还需要继续熟悉练习，其中堆的概念，以及实现需要认真理解。
