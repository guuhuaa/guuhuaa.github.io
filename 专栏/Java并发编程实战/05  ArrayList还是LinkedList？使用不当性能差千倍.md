<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05  ArrayList还是LinkedList？使用不当性能差千倍.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词你为什么需要学习并发编程？.md">00 开篇词你为什么需要学习并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;如何制定性能调优标准？.md">01  如何制定性能调优标准？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;如何制定性能调优策略？.md">02  如何制定性能调优策略？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;字符串性能优化不容小觑，百M内存轻松存储几十G数据.md">03  字符串性能优化不容小觑，百M内存轻松存储几十G数据.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;慎重使用正则表达式.md">04  慎重使用正则表达式.md</a>

                </li>
                <li>

                    <a class="current-tab" href="05&#32;&#32;ArrayList还是LinkedList？使用不当性能差千倍.md">05  ArrayList还是LinkedList？使用不当性能差千倍.md</a>
                    

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Stream如何提高遍历集合效率？.md">06  Stream如何提高遍历集合效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入浅出HashMap的设计与优化.md">07  深入浅出HashMap的设计与优化.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md">08  网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;网络通信优化之序列化：避免使用Java序列化.md">09  网络通信优化之序列化：避免使用Java序列化.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;网络通信优化之通信协议：如何优化RPC网络通信？.md">10  网络通信优化之通信协议：如何优化RPC网络通信？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;答疑课堂：深入了解NIO的优化实现原理.md">11  答疑课堂：深入了解NIO的优化实现原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md">12  多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md">13  多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;多线程之锁优化（下）：使用乐观锁优化并行操作.md">14  多线程之锁优化（下）：使用乐观锁优化并行操作.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;多线程调优（上）：哪些操作导致了上下文切换？.md">15  多线程调优（上）：哪些操作导致了上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;多线程调优（下）：如何优化多线程上下文切换？.md">16  多线程调优（下）：如何优化多线程上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;并发容器的使用：识别不同场景下最优容器.md">17  并发容器的使用：识别不同场景下最优容器.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何设置线程池大小？.md">18  如何设置线程池大小？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何用协程来优化多线程业务？.md">19  如何用协程来优化多线程业务？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md">20  磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深入JVM即时编译器JIT，优化Java编译.md">21  深入JVM即时编译器JIT，优化Java编译.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;如何优化垃圾回收机制？.md">22  如何优化垃圾回收机制？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;如何优化JVM内存分配？.md">23  如何优化JVM内存分配？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;内存持续上升，我该如何排查问题？.md">24  内存持续上升，我该如何排查问题？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;答疑课堂：模块四热点问题解答.md">25  答疑课堂：模块四热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;单例模式：如何创建单一对象优化系统性能？.md">26  单例模式：如何创建单一对象优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;原型模式与享元模式：提升系统性能的利器.md">27  原型模式与享元模式：提升系统性能的利器.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;如何使用设计模式优化并发编程？.md">28  如何使用设计模式优化并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;生产者消费者模式：电商库存设计优化.md">29  生产者消费者模式：电商库存设计优化.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;装饰器模式：如何优化电商系统中复杂的商品价格策略？.md">30  装饰器模式：如何优化电商系统中复杂的商品价格策略？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;答疑课堂：模块五思考题集锦.md">31  答疑课堂：模块五思考题集锦.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;MySQL调优之SQL语句：如何写出高性能SQL语句？.md">32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;MySQL调优之事务：高并发场景下的数据库事务调优.md">33  MySQL调优之事务：高并发场景下的数据库事务调优.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;MySQL调优之索引：索引的失效与优化.md">34  MySQL调优之索引：索引的失效与优化.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;记一次线上SQL死锁事故：如何避免死锁？.md">35  记一次线上SQL死锁事故：如何避免死锁？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;什么时候需要分表分库？.md">36  什么时候需要分表分库？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;电商系统表设计优化案例分析.md">37  电商系统表设计优化案例分析.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;数据库参数设置优化，失之毫厘差之千里.md">38  数据库参数设置优化，失之毫厘差之千里.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;答疑课堂：MySQL中InnoDB的知识点串讲.md">39  答疑课堂：MySQL中InnoDB的知识点串讲.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;如何设计更优的分布式锁？.md">41  如何设计更优的分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;电商系统的分布式事务调优.md">42  电商系统的分布式事务调优.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;如何使用缓存优化系统性能？.md">43  如何使用缓存优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;记一次双十一抢购性能瓶颈调优.md">44  记一次双十一抢购性能瓶颈调优.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;什么是数据的强、弱一致性？.md">加餐  什么是数据的强、弱一致性？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;推荐几款常用的性能测试工具.md">加餐  推荐几款常用的性能测试工具.md</a>

                </li>
                <li>

                    
                    <a href="答疑课堂：模块三热点问题解答.md">答疑课堂：模块三热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;栉风沐雨，砥砺前行！.md">结束语  栉风沐雨，砥砺前行！.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>05  ArrayList还是LinkedList？使用不当性能差千倍</h1>
<p>你好，我是刘超。</p>
<p>集合作为一种存储数据的容器，是我们日常开发中使用最频繁的对象类型之一。JDK 为开发者提供了一系列的集合类型，这些集合类型使用不同的数据结构来实现。因此，不同的集合类型，使用场景也不同。</p>
<p>很多同学在面试的时候，经常会被问到集合的相关问题，比较常见的有 ArrayList 和 LinkedList 的区别。</p>
<p>相信大部分同学都能回答上：“ArrayList 是基于数组实现，LinkedList 是基于链表实现。”</p>
<p>而在回答使用场景的时候，我发现大部分同学的答案是：“ArrayList 和 LinkedList 在新增、删除元素时，LinkedList 的效率要高于 ArrayList，而在遍历的时候，ArrayList 的效率要高于 LinkedList。”这个回答是否准确呢？今天这一讲就带你验证。</p>
<h2>初识 List 接口</h2>
<p>在学习 List 集合类之前，我们先来通过这张图，看下 List 集合类的接口和类的实现关系：</p>
<p><img src="assets/ab73021caa4545ae0ac917e0f36cde36.jpg" alt="img" /></p>
<p>我们可以看到 ArrayList、Vector、LinkedList 集合类继承了 AbstractList 抽象类，而 AbstractList 实现了 List 接口，同时也继承了 AbstractCollection 抽象类。ArrayList、Vector、LinkedList 又根据自我定位，分别实现了各自的功能。</p>
<p>ArrayList 和 Vector 使用了数组实现，这两者的实现原理差不多，LinkedList 使用了双向链表实现。基础铺垫就到这里，接下来，我们就详细地分析下 ArrayList 和 LinkedList 的源码实现。</p>
<h2>ArrayList 是如何实现的？</h2>
<p>ArrayList 很常用，先来几道测试题，自检下你对 ArrayList 的了解程度。</p>
<p>**问题 1：**我们在查看 ArrayList 的实现类源码时，你会发现对象数组 elementData 使用了 transient 修饰，我们知道 transient 关键字修饰该属性，则表示该属性不会被序列化，然而我们并没有看到文档中说明 ArrayList 不能被序列化，这是为什么？</p>
<p>**问题 2：**我们在使用 ArrayList 进行新增、删除时，经常被提醒“使用 ArrayList 做新增删除操作会影响效率”。那是不是 ArrayList 在大量新增元素的场景下效率就一定会变慢呢？</p>
<p>**问题 3：**如果让你使用 for 循环以及迭代循环遍历一个 ArrayList，你会使用哪种方式呢？原因是什么？</p>
<p>如果你对这几道测试都没有一个全面的了解，那就跟我一起从数据结构、实现原理以及源码角度重新认识下 ArrayList 吧。</p>
<h3>1.ArrayList 实现类</h3>
<p>ArrayList 实现了 List 接口，继承了 AbstractList 抽象类，底层是数组实现的，并且实现了自增扩容数组大小。</p>
<p>ArrayList 还实现了 Cloneable 接口和 Serializable 接口，所以他可以实现克隆和序列化。</p>
<p>ArrayList 还实现了 RandomAccess 接口。你可能对这个接口比较陌生，不知道具体的用处。通过代码我们可以发现，这个接口其实是一个空接口，什么也没有实现，那 ArrayList 为什么要去实现它呢？</p>
<p>其实 RandomAccess 接口是一个标志接口，他标志着“只要实现该接口的 List 类，都能实现快速随机访问”。</p>
<pre><code>public class ArrayList&lt;E&gt; extends AbstractList&lt;E&gt;
        implements List&lt;E&gt;, RandomAccess, Cloneable, java.io.Serializable
</code></pre>
<h3>2.ArrayList 属性</h3>
<p>ArrayList 属性主要由数组长度 size、对象数组 elementData、初始化容量 default_capacity 等组成， 其中初始化容量默认大小为 10。</p>
<pre><code>  // 默认初始化容量
    private static final int DEFAULT_CAPACITY = 10;
    // 对象数组
    transient Object[] elementData; 
    // 数组长度
    private int size;
</code></pre>
<p>从 ArrayList 属性来看，它没有被任何的多线程关键字修饰，但 elementData 被关键字 transient 修饰了。这就是我在上面提到的第一道测试题：transient 关键字修饰该字段则表示该属性不会被序列化，但 ArrayList 其实是实现了序列化接口，这到底是怎么回事呢？</p>
<p>这还得从“ArrayList 是基于数组实现“开始说起，由于 ArrayList 的数组是基于动态扩增的，所以并不是所有被分配的内存空间都存储了数据。</p>
<p>如果采用外部序列化法实现数组的序列化，会序列化整个数组。ArrayList 为了避免这些没有存储数据的内存空间被序列化，内部提供了两个私有方法 writeObject 以及 readObject 来自我完成序列化与反序列化，从而在序列化与反序列化数组时节省了空间和时间。</p>
<p>因此使用 transient 修饰数组，是防止对象数组被其他外部方法序列化。</p>
<h3>3.ArrayList 构造函数</h3>
<p>ArrayList 类实现了三个构造函数，第一个是创建 ArrayList 对象时，传入一个初始化值；第二个是默认创建一个空数组对象；第三个是传入一个集合类型进行初始化。</p>
<p>当 ArrayList 新增元素时，如果所存储的元素已经超过其已有大小，它会计算元素大小后再进行动态扩容，数组的扩容会导致整个数组进行一次内存复制。因此，我们在初始化 ArrayList 时，可以通过第一个构造函数合理指定数组初始大小，这样有助于减少数组的扩容次数，从而提高系统性能。</p>
<pre><code> public ArrayList(int initialCapacity) {
        // 初始化容量不为零时，将根据初始化值创建数组大小
        if (initialCapacity &gt; 0) {
            this.elementData = new Object[initialCapacity];
        } else if (initialCapacity == 0) {// 初始化容量为零时，使用默认的空数组
            this.elementData = EMPTY_ELEMENTDATA;
        } else {
            throw new IllegalArgumentException(&quot;Illegal Capacity: &quot;+
                                               initialCapacity);
        }
    }
 
    public ArrayList() {
        // 初始化默认为空数组
        this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;
    }
</code></pre>
<h3>4.ArrayList 新增元素</h3>
<p>ArrayList 新增元素的方法有两种，一种是直接将元素加到数组的末尾，另外一种是添加元素到任意位置。</p>
<pre><code> public boolean add(E e) {
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }
 
    public void add(int index, E element) {
        rangeCheckForAdd(index);
 
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        System.arraycopy(elementData, index, elementData, index + 1,
                         size - index);
        elementData[index] = element;
        size++;
    }
</code></pre>
<p>两个方法的相同之处是在添加元素之前，都会先确认容量大小，如果容量够大，就不用进行扩容；如果容量不够大，就会按照原来数组的 1.5 倍大小进行扩容，在扩容之后需要将数组复制到新分配的内存地址。</p>
<pre><code>  private void ensureExplicitCapacity(int minCapacity) {
        modCount++;
 
        // overflow-conscious code
        if (minCapacity - elementData.length &gt; 0)
            grow(minCapacity);
    }
    private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;
 
    private void grow(int minCapacity) {
        // overflow-conscious code
        int oldCapacity = elementData.length;
        int newCapacity = oldCapacity + (oldCapacity &gt;&gt; 1);
        if (newCapacity - minCapacity &lt; 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE &gt; 0)
            newCapacity = hugeCapacity(minCapacity);
        // minCapacity is usually close to size, so this is a win:
        elementData = Arrays.copyOf(elementData, newCapacity);
    }
</code></pre>
<p>当然，两个方法也有不同之处，添加元素到任意位置，会导致在该位置后的所有元素都需要重新排列，而将元素添加到数组的末尾，在没有发生扩容的前提下，是不会有元素复制排序过程的。</p>
<p>这里你就可以找到第二道测试题的答案了。如果我们在初始化时就比较清楚存储数据的大小，就可以在 ArrayList 初始化时指定数组容量大小，并且在添加元素时，只在数组末尾添加元素，那么 ArrayList 在大量新增元素的场景下，性能并不会变差，反而比其他 List 集合的性能要好。</p>
<h3>5.ArrayList 删除元素</h3>
<p>ArrayList 的删除方法和添加任意位置元素的方法是有些相同的。ArrayList 在每一次有效的删除元素操作之后，都要进行数组的重组，并且删除的元素位置越靠前，数组重组的开销就越大。</p>
<pre><code> public E remove(int index) {
        rangeCheck(index);
 
        modCount++;
        E oldValue = elementData(index);
 
        int numMoved = size - index - 1;
        if (numMoved &gt; 0)
            System.arraycopy(elementData, index+1, elementData, index,
                             numMoved);
        elementData[--size] = null; // clear to let GC do its work
 
        return oldValue;
    }
</code></pre>
<h3>6.ArrayList 遍历元素</h3>
<p>由于 ArrayList 是基于数组实现的，所以在获取元素的时候是非常快捷的。</p>
<pre><code>  public E get(int index) {
        rangeCheck(index);
 
        return elementData(index);
    }
 
    E elementData(int index) {
        return (E) elementData[index];
    }
</code></pre>
<h2>LinkedList 是如何实现的？</h2>
<p>虽然 LinkedList 与 ArrayList 都是 List 类型的集合，但 LinkedList 的实现原理却和 ArrayList 大相径庭，使用场景也不太一样。</p>
<p>LinkedList 是基于双向链表数据结构实现的，LinkedList 定义了一个 Node 结构，Node 结构中包含了 3 个部分：元素内容 item、前指针 prev 以及后指针 next，代码如下。</p>
<pre><code> private static class Node&lt;E&gt; {
        E item;
        Node&lt;E&gt; next;
        Node&lt;E&gt; prev;
 
        Node(Node&lt;E&gt; prev, E element, Node&lt;E&gt; next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
</code></pre>
<p>总结一下，LinkedList 就是由 Node 结构对象连接而成的一个双向链表。在 JDK1.7 之前，LinkedList 中只包含了一个 Entry 结构的 header 属性，并在初始化的时候默认创建一个空的 Entry，用来做 header，前后指针指向自己，形成一个循环双向链表。</p>
<p>在 JDK1.7 之后，LinkedList 做了很大的改动，对链表进行了优化。链表的 Entry 结构换成了 Node，内部组成基本没有改变，但 LinkedList 里面的 header 属性去掉了，新增了一个 Node 结构的 first 属性和一个 Node 结构的 last 属性。这样做有以下几点好处：</p>
<ul>
<li>first/last 属性能更清晰地表达链表的链头和链尾概念；</li>
<li>first/last 方式可以在初始化 LinkedList 的时候节省 new 一个 Entry；</li>
<li>first/last 方式最重要的性能优化是链头和链尾的插入删除操作更加快捷了。</li>
</ul>
<p>这里同 ArrayList 的讲解一样，我将从数据结构、实现原理以及源码分析等几个角度带你深入了解 LinkedList。</p>
<h3>1.LinkedList 实现类</h3>
<p>LinkedList 类实现了 List 接口、Deque 接口，同时继承了 AbstractSequentialList 抽象类，LinkedList 既实现了 List 类型又有 Queue 类型的特点；LinkedList 也实现了 Cloneable 和 Serializable 接口，同 ArrayList 一样，可以实现克隆和序列化。</p>
<p>由于 LinkedList 存储数据的内存地址是不连续的，而是通过指针来定位不连续地址，因此，LinkedList 不支持随机快速访问，LinkedList 也就不能实现 RandomAccess 接口。</p>
<pre><code>public class LinkedList&lt;E&gt;
    extends AbstractSequentialList&lt;E&gt;
    implements List&lt;E&gt;, Deque&lt;E&gt;, Cloneable, java.io.Serializable
</code></pre>
<h3>2.LinkedList 属性</h3>
<p>我们前面讲到了 LinkedList 的两个重要属性 first/last 属性，其实还有一个 size 属性。我们可以看到这三个属性都被 transient 修饰了，原因很简单，我们在序列化的时候不会只对头尾进行序列化，所以 LinkedList 也是自行实现 readObject 和 writeObject 进行序列化与反序列化。</p>
<pre><code>  transient int size = 0;
    transient Node&lt;E&gt; first;
    transient Node&lt;E&gt; last;
</code></pre>
<h3>3.LinkedList 新增元素</h3>
<p>LinkedList 添加元素的实现很简洁，但添加的方式却有很多种。默认的 add (Ee) 方法是将添加的元素加到队尾，首先是将 last 元素置换到临时变量中，生成一个新的 Node 节点对象，然后将 last 引用指向新节点对象，之前的 last 对象的前指针指向新节点对象。</p>
<pre><code> public boolean add(E e) {
        linkLast(e);
        return true;
    }
 
    void linkLast(E e) {
        final Node&lt;E&gt; l = last;
        final Node&lt;E&gt; newNode = new Node&lt;&gt;(l, e, null);
        last = newNode;
        if (l == null)
            first = newNode;
        else
            l.next = newNode;
        size++;
        modCount++;
    }
</code></pre>
<p>LinkedList 也有添加元素到任意位置的方法，如果我们是将元素添加到任意两个元素的中间位置，添加元素操作只会改变前后元素的前后指针，指针将会指向添加的新元素，所以相比 ArrayList 的添加操作来说，LinkedList 的性能优势明显。</p>
<pre><code> public void add(int index, E element) {
        checkPositionIndex(index);
 
        if (index == size)
            linkLast(element);
        else
            linkBefore(element, node(index));
    }
 
    void linkBefore(E e, Node&lt;E&gt; succ) {
        // assert succ != null;
        final Node&lt;E&gt; pred = succ.prev;
        final Node&lt;E&gt; newNode = new Node&lt;&gt;(pred, e, succ);
        succ.prev = newNode;
        if (pred == null)
            first = newNode;
        else
            pred.next = newNode;
        size++;
        modCount++;
    }
</code></pre>
<h3>4.LinkedList 删除元素</h3>
<p>在 LinkedList 删除元素的操作中，我们首先要通过循环找到要删除的元素，如果要删除的位置处于 List 的前半段，就从前往后找；若其位置处于后半段，就从后往前找。</p>
<p>这样做的话，无论要删除较为靠前或较为靠后的元素都是非常高效的，但如果 List 拥有大量元素，移除的元素又在 List 的中间段，那效率相对来说会很低。</p>
<h3>5.LinkedList 遍历元素</h3>
<p>LinkedList 的获取元素操作实现跟 LinkedList 的删除元素操作基本类似，通过分前后半段来循环查找到对应的元素。但是通过这种方式来查询元素是非常低效的，特别是在 for 循环遍历的情况下，每一次循环都会去遍历半个 List。</p>
<p>所以在 LinkedList 循环遍历时，我们可以使用 iterator 方式迭代循环，直接拿到我们的元素，而不需要通过循环查找 List。</p>
<h2>总结</h2>
<p>前面我们已经从源码的实现角度深入了解了 ArrayList 和 LinkedList 的实现原理以及各自的特点。如果你能充分理解这些内容，很多实际应用中的相关性能问题也就迎刃而解了。</p>
<p>就像如果现在还有人跟你说，“ArrayList 和 LinkedList 在新增、删除元素时，LinkedList 的效率要高于 ArrayList，而在遍历的时候，ArrayList 的效率要高于 LinkedList”，你还会表示赞同吗？</p>
<p>现在我们不妨通过几组测试来验证一下。这里因为篇幅限制，所以我就直接给出测试结果了，对应的测试代码你可以访问<a href="https://github.com/nickliuchao/collection">Github</a>查看和下载。</p>
<p><strong>1.ArrayList 和 LinkedList 新增元素操作测试</strong></p>
<ul>
<li>从集合头部位置新增元素</li>
<li>从集合中间位置新增元素</li>
<li>从集合尾部位置新增元素</li>
</ul>
<p>测试结果 (花费时间)：</p>
<ul>
<li>ArrayList&gt;LinkedList</li>
<li>ArrayList&lt;LinkedList</li>
<li>ArrayList&lt;LinkedList</li>
</ul>
<p>通过这组测试，我们可以知道 LinkedList 添加元素的效率未必要高于 ArrayList。</p>
<p>由于 ArrayList 是数组实现的，而数组是一块连续的内存空间，在添加元素到数组头部的时候，需要对头部以后的数据进行复制重排，所以效率很低；而 LinkedList 是基于链表实现，在添加元素的时候，首先会通过循环查找到添加元素的位置，如果要添加的位置处于 List 的前半段，就从前往后找；若其位置处于后半段，就从后往前找。因此 LinkedList 添加元素到头部是非常高效的。</p>
<p>同上可知，ArrayList 在添加元素到数组中间时，同样有部分数据需要复制重排，效率也不是很高；LinkedList 将元素添加到中间位置，是添加元素最低效率的，因为靠近中间位置，在添加元素之前的循环查找是遍历元素最多的操作。</p>
<p>而在添加元素到尾部的操作中，我们发现，在没有扩容的情况下，ArrayList 的效率要高于 LinkedList。这是因为 ArrayList 在添加元素到尾部的时候，不需要复制重排数据，效率非常高。而 LinkedList 虽然也不用循环查找元素，但 LinkedList 中多了 new 对象以及变换指针指向对象的过程，所以效率要低于 ArrayList。</p>
<p>说明一下，这里我是基于 ArrayList 初始化容量足够，排除动态扩容数组容量的情况下进行的测试，如果有动态扩容的情况，ArrayList 的效率也会降低。</p>
<p><strong>2.ArrayList 和 LinkedList 删除元素操作测试</strong></p>
<ul>
<li>从集合头部位置删除元素</li>
<li>从集合中间位置删除元素</li>
<li>从集合尾部位置删除元素</li>
</ul>
<p>测试结果 (花费时间)：</p>
<ul>
<li>ArrayList&gt;LinkedList</li>
<li>ArrayList&lt;LinkedList</li>
<li>ArrayList&lt;LinkedList</li>
</ul>
<p>ArrayList 和 LinkedList 删除元素操作测试的结果和添加元素操作测试的结果很接近，这是一样的原理，我在这里就不重复讲解了。</p>
<p><strong>3.ArrayList 和 LinkedList 遍历元素操作测试</strong></p>
<ul>
<li>for(;;) 循环</li>
<li>迭代器迭代循环</li>
</ul>
<p>测试结果 (花费时间)：</p>
<ul>
<li>ArrayList&lt;LinkedList</li>
<li>ArrayList≈LinkedList</li>
</ul>
<p>我们可以看到，LinkedList 的 for 循环性能是最差的，而 ArrayList 的 for 循环性能是最好的。</p>
<p>这是因为 LinkedList 基于链表实现的，在使用 for 循环的时候，每一次 for 循环都会去遍历半个 List，所以严重影响了遍历的效率；ArrayList 则是基于数组实现的，并且实现了 RandomAccess 接口标志，意味着 ArrayList 可以实现快速随机访问，所以 for 循环效率非常高。</p>
<p>LinkedList 的迭代循环遍历和 ArrayList 的迭代循环遍历性能相当，也不会太差，所以在遍历 LinkedList 时，我们要切忌使用 for 循环遍历。</p>
<h2>思考题</h2>
<p>我们通过一个使用 for 循环遍历删除操作 ArrayList 数组的例子，思考下 ArrayList 数组的删除操作应该注意的一些问题。</p>
<pre><code>public static void main(String[] args)
    {
        ArrayList&lt;String&gt; list = new ArrayList&lt;String&gt;();
        list.add(&quot;a&quot;);
        list.add(&quot;a&quot;);
        list.add(&quot;b&quot;);
        list.add(&quot;b&quot;);
        list.add(&quot;c&quot;);
        list.add(&quot;c&quot;);
        remove(list);// 删除指定的“b”元素
 
        for(int i=0; i&lt;list.size(); i++)(&quot;c&quot;)()()(s : list) 
        {
            System.out.println(&quot;element : &quot; + s)list.get(i)
        }
    }
</code></pre>
<p>从上面的代码来看，我定义了一个 ArrayList 数组，里面添加了一些元素，然后我通过 remove 删除指定的元素。请问以下两种写法，哪种是正确的？</p>
<p>写法 1：</p>
<pre><code>public static void remove(ArrayList&lt;String&gt; list) 
    {
        Iterator&lt;String&gt; it = list.iterator();
        
        while (it.hasNext()) {
            String str = it.next();
            
            if (str.equals(&quot;b&quot;)) {
                it.remove();
            }
        }
 
    }
</code></pre>
<p>写法 2：</p>
<pre><code>public static void remove(ArrayList&lt;String&gt; list) 
    {
        for (String s : list)
        {
            if (s.equals(&quot;b&quot;)) 
            {
                list.remove(s);
            }
        }
    }
</code></pre>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;&#32;慎重使用正则表达式.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;&#32;Stream如何提高遍历集合效率？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4343c29ce770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
