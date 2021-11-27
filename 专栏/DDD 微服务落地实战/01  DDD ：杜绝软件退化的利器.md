<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>01  DDD ：杜绝软件退化的利器.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;让我们把&#32;DDD&#32;的思想真正落地.md">00 开篇词  让我们把 DDD 的思想真正落地.md</a>

                </li>
                <li>

                    <a class="current-tab" href="01&#32;&#32;DDD&#32;：杜绝软件退化的利器.md">01  DDD ：杜绝软件退化的利器.md</a>
                    

                </li>
                <li>

                    
                    <a href="02&#32;&#32;以电商支付功能为例演练&#32;DDD.md">02  以电商支付功能为例演练 DDD.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;DDD&#32;是如何落地到数据库设计的？.md">03  DDD 是如何落地到数据库设计的？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;领域模型是如何指导程序设计的？.md">04  领域模型是如何指导程序设计的？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;聚合、仓库与工厂：傻傻分不清楚.md">05  聚合、仓库与工厂：傻傻分不清楚.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;限界上下文：冲破微服务设计困局的利器.md">06  限界上下文：冲破微服务设计困局的利器.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;在线订餐场景中是如何开事件风暴会议的？.md">07  在线订餐场景中是如何开事件风暴会议的？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;DDD&#32;是如何解决微服务拆分难题的？.md">08  DDD 是如何解决微服务拆分难题的？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;DDD&#32;是如何落地微服务设计实现的？.md">09  DDD 是如何落地微服务设计实现的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;微服务落地的技术实践.md">10  微服务落地的技术实践.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;解决技术改造困局的钥匙：整洁架构.md">11  解决技术改造困局的钥匙：整洁架构.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何设计支持快速交付的技术中台战略？.md">12  如何设计支持快速交付的技术中台战略？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;如何实现支持快速交付的技术中台设计？.md">13  如何实现支持快速交付的技术中台设计？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何设计支持&#32;DDD&#32;的技术中台？.md">14  如何设计支持 DDD 的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">15  如何设计支持微服务的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;基于&#32;DDD&#32;的微服务设计演示（含支持微服务的&#32;DDD&#32;技术中台设计）.md">17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;基于事件溯源的设计开发.md">18  基于事件溯源的设计开发.md</a>

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
                        <div><h1>01  DDD ：杜绝软件退化的利器</h1>
<p>2004 年，软件大师 Eric Evans 的不朽著作《领域驱动设计：软件核心复杂性应对之道》面世，从书名可以看出，这是一本应对软件系统越来越复杂的方法论的图书。然而，在当时，中国的软件业才刚刚起步，软件系统还没有那么复杂，即使维护了几年，软件退化了，不好维护了，推倒重新开发就好了。因此，在过去的那么多年里，真正运用领域驱动设计开发（DDD）的团队并不多。一套优秀的方法论，因为现实阶段原因而一直不温不火。</p>
<p>不过，这些年随着中国软件业的快速发展，软件规模越来越大，生命周期也越来越长，推倒重新开发的风险越来越大。这时，软件团队急切需要在较低成本的状态下持续维护一个系统很多年。然而，事与愿违。随着时间的推移，程序越来越乱，维护成本越来越高，软件退化成了无数软件团队的噩梦。</p>
<p>这时，微服务架构成了规模化软件的解决之道。不过，<strong>微服务对设计提出了很高的要求，强调“小而专、高内聚”，否则就不能发挥出微服务的优势，甚至可能令问题更糟糕</strong>。</p>
<p>因此，微服务的设计，微服务的拆分都需要领域驱动设计的指导。那么，<strong>领域驱动为什么能解决软件规模化的问题呢？</strong> 我们先从问题的根源谈起，即软件退化。</p>
<h3>软件退化的根源</h3>
<p>最近 10 年的互联网发展，从电子商务到移动互联，再到“互联网+”与传统行业的互联网转型，是一个非常痛苦的转型过程。而近几年的人工智能与 5G 技术的发展，又会带动整个产业向着大数据与物联网发展，另一轮的技术转型已经拉开帷幕。</p>
<p>那么，在这个过程中，一方面会给我们带来诸多的挑战，另一方面又会给我们带来无尽的机会，它会带来更多的新兴市场、新兴产业与全新业务，给我们带来全新的发展机遇。</p>
<p>然而，在面对全新业务、全新增长点的时候，我们能不能把握住这样的机遇呢？我们期望能把握住，但每次回到现实，回到正在维护的系统时，却令人沮丧。我们的软件总是经历着这样的轮回，<strong>软件设计质量最高的时候是第一次设计的那个版本，当第一个版本设计上线以后就开始各种需求变更，这常常又会打乱原有的设计。</strong></p>
<p>因此，需求变更一次，软件就修改一次，软件修改一次，质量就下降一次。不论第一次的设计质量有多高，软件经历不了几次变更，就进入一种低质量、难以维护的状态。进而，团队就不得不在这样的状态下，以高成本的方式不断地维护下去，维护很多年。</p>
<p>这时候，维护好原有的业务都非常不易，又如何再去期望未来更多的全新业务呢？比如，这是一段电商网站支付功能的设计，最初的版本设计质量还是不错的：</p>
<p><img src="assets/Ciqc1F-uW4mAMW8uAACi9O_bw00391.png" alt="Drawing 0.png" /></p>
<p>当第一个版本上线以后，很快就迎来了第一次变更，变更的需求是增加商品折扣功能，并且这个折扣功能还要分为限时折扣、限量折扣、某类商品的折扣、某个商品的折扣。当我们拿到这个需求时怎么做呢？很简单，增加一个 if 语句，if 限时折扣就怎么怎么样，if 限量折扣就怎么怎么样……代码开始膨胀了。</p>
<p>接着，第二次变更需要增加 VIP 会员，除了增加各种金卡、银卡的折扣，还要为会员发放各种福利，让会员享受各种特权。为了实现这些需求，我们又要在 payoff() 方法中加入更多的代码。</p>
<p>第三次变更增加的是支付方式，除了支付宝支付，还要增加微信支付、各种银行卡支付、各种支付平台支付，此时又要塞入一大堆代码。经过这三次变更，你可以想象现在的 payoff() 方法是什么样子了吧，变更是不是就可以结束了呢？其实不能，接着还要增加更多的秒杀、预订、闪购、众筹，以及各种返券。程序变得越来越乱而难以阅读，每次变更也变得越来越困难。</p>
<p><img src="assets/Ciqc1F-uXAqAZkZ9AAMBEqyGMVU564.png" alt="图片3" /></p>
<p>问题来了：为什么软件会退化，会随着变更而设计质量下降呢？在这个问题上，我们必须寻找到问题的根源，才能对症下药、解决问题。</p>
<p>要探寻软件退化的根源，先要从探寻软件的本质及其规律开始，软件的本质就是对真实世界的模拟，每个软件都能在真实世界中找到它的影子。因此，软件中业务逻辑正确与否的唯一标准就是<strong>是否与真实世界一致</strong>。如果一致，则软件是 OK 的；不一致，则用户会提 Bug、提新需求。</p>
<p>在这里发现了一个非常重要的线索，那就是，<strong>软件要做成什么样，既不由我们来决定，也不由用户来决定，而是由客观世界决定</strong>。用户为什么总在改需求，是因为他们也不确定客观世界的规则，只有遇到问题了他们才能想得起来。因此，对于我们来说，与其唯唯诺诺地按照用户的要求去做软件，不如主动地理解业务的基础上去分析软件，而后者会更有利于我们减少变更的成本。</p>
<p>那么，真实世界是怎样，我们就怎样开发软件，不就简单了吗？其实并非如此，因为真实世界是非常复杂的，要深刻理解真实世界中的这些业务逻辑是需要一个过程的。因此，我们最初只能认识真实世界中那些简单、清晰、易于理解的业务逻辑，把它们做到我们的软件里，即每个软件的第一个版本的需求总是那么清晰明了、易于设计。</p>
<p>然而，当我们把第一个版本的软件交付用户使用的时候，用户却会发现，还有很多不简单、不明了、不易于理解的业务逻辑没做到软件里。这在使用软件的过程中很不方便，和真实业务不一致，因此用户就会提 Bug、提新需求。</p>
<p><strong>在我们不断地修复 Bug，实现新需求的过程中，软件的业务逻辑也会越来越接近真实世界，使得我们的软件越来越专业，让用户感觉越来越好用。但是，在软件越来越接近真实世界的过程中，业务逻辑就会变得越来越复杂，软件规模也越来越庞大</strong>。</p>
<p>你一定有这样一个认识：简单软件有简单软件的设计，复杂软件有复杂软件的设计。</p>
<p>比如，现在的需求就是将用户订单按照“单价 × 数量”公式来计算应付金额，那么在一个 PaymentBus 类中增加一个 payoff() 方法即可，这样的设计没有问题。不过，如果现在的需求需要在付款的过程中计算各种折扣、各种优惠、各种返券，那么我们必然会做成一个复杂的程序结构。</p>
<p><img src="assets/Ciqc1F-x5CiASyG1AAFOkD8Rz1U365.png" alt="Lark20201116-102936.png" /></p>
<p>但是，真实情况却不是这样的。真实情况是，起初我们拿到的需求是那个简单需求，然后在简单需求的基础上进行了设计开发。但随着软件的不断变更，软件业务逻辑变得越来越复杂，软件规模不断扩大，逐渐由一个简单软件转变成一个复杂软件。</p>
<p>这时，如果要保持软件设计质量不退化，就应当逐步调整软件的程序结构，逐渐由简单的程序结构转变为复杂的程序结构。如果我们总是这样做，就能始终保持软件的设计质量，不过非常遗憾的是，我们以往在维护软件的过程中却不是这样做的，而是不断地在原有简单软件的程序结构下，往 payoff() 方法中塞代码，这样做必然会造成软件的退化。</p>
<p>也就是说，<strong>软件退化的根源不是软件变更，软件变更只是一个诱因</strong>。如果每次软件变更时，适时地进行解耦，进行功能扩展，再实现新的功能，就能保持高质量的软件设计。但如果在每次软件变更时没有调整程序结构，而是在原有的程序结构上不断地塞代码，软件就会退化。这就是软件发展的规律，软件退化的根源。</p>
<h3>杜绝软件退化：两顶帽子</h3>
<p>前面谈到，要保持软件设计质量不退化，必须在每次需求变更的时候，对原有的程序结构适当地进行调整。那么应当怎样进行调整呢？还是回到前面电商网站付款功能的那个案例，看看每次需求变更应当怎样设计。</p>
<p>在交付第一个版本的基础上，很快第一次需求变更就到来了。第一次需求变更的内容如下。</p>
<p>增加商品折扣功能，该功能分为以下几种类型：</p>
<ul>
<li>限时折扣</li>
<li>限量折扣</li>
<li>对某类商品进行折扣</li>
<li>对某个商品进行折扣</li>
<li>不折扣</li>
</ul>
<p>以往我们拿到这个需求，就很不冷静地开始改代码，修改成了如下一段代码：</p>
<p><img src="assets/Ciqc1F-uXC2APP3nAAFByY8Jh7U062.png" alt="Drawing 3.png" /></p>
<p>这里增加了一段 if 语句，并不是一种好的变更方式。如果每次都这样变更，那么软件必然就会退化，进入难以维护的状态。这种变更为什么就不好呢？因为它违反了“开放-封闭原则”。</p>
<p><strong>开放-封闭原则（OCP）</strong> 分为开放原则与封闭原则两部分。</p>
<ul>
<li><strong>开放原则</strong>：我们开发的软件系统，对于功能扩展是开放的（Open for Extension），即当系统需求发生变更时，可以对软件功能进行扩展，使其满足用户新的需求。</li>
<li><strong>封闭原则</strong>：对软件代码的修改应当是封闭的（Close for Modification），即在修改软件的同时，不要影响到系统原有的功能，所以应当在不修改原有代码的基础上实现新的功能。也就是说，在增加新功能的时候，新代码与老代码应当隔离，不能在同一个类、同一个方法中。</li>
</ul>
<p>前面的设计，在实现新功能的同时，新代码与老代码在同一个类、同一个方法中了，违反了“开放-封闭原则”。怎样才能既满足“开放-封闭原则”，又能够实现新功能呢？在原有的代码上你发现什么都做不了！难道“开放-封闭原则”错了吗？</p>
<p>问题的关键就在于，当我们在实现新需求时，应当采用“两顶帽子”的方式进行设计，这种方式就要求在每次变更时，将变更分为两个步骤。</p>
<p><strong>两顶帽子</strong>：</p>
<ul>
<li>在不添加新功能的前提下，重构代码，调整原有程序结构，以适应新功能；</li>
<li>实现新的功能。</li>
</ul>
<p>按以上案例为例，为了实现新的功能，我们在原有代码的基础上，在不添加新功能的前提下调整原有程序结构，我们抽取出了 Strategy 这样一个接口和“不折扣”这个实现类。这时，原有程序变了吗？没有。但是程序结构却变了，增加了这样一个接口，称为“可扩展点”。在这个可扩展点的基础上再实现各种折扣，既能满足“开放-封闭原则”来保证程序质量，又能够满足新的需求。当日后发生新的变更时，什么类型的折扣就修改哪个实现类，添加新的折扣类型就增加新的实现类，维护成本得到降低。</p>
<p><img src="assets/Ciqc1F-uXESAX4mlAAHXdslwIpQ810.png" alt="Drawing 4.png" /></p>
<p>“两顶帽子”的设计方式意义重大。过去，我们每次在设计软件时总是担心日后的变更，就很不冷静地设计了很多所谓的“灵活设计”。然而，每一种“灵活设计”只能应对一种需求变更，而我们又不是先知，不知道日后会发生什么样的变更。最后的结果就是，我们期望的变更并没有发生，所做的设计都变成了摆设，它既不起什么作用，还增加了程序复杂度；我们没有期望的变更发生了，原有的程序依然不能解决新的需求，程序又被打回了原形。因此，这样的设计不能真正解决未来变更的问题，被称为“<strong>过度设计</strong>”。</p>
<p><strong>有了“两顶帽子”，我们不再需要焦虑，不再需要过度设计</strong>，正确的思路应当是“活在今天的格子里做今天的事儿”，也就是为当前的需求进行设计，使其刚刚满足当前的需求。所谓的“高质量的软件设计”就是要掌握一个平衡，一方面要满足当前的需求，另一方面要让设计刚刚满足需求，从而使设计最简化、代码最少。这样做，不仅软件设计质量提高了，设计难点也得到了大幅度降低。</p>
<p>简而言之，<strong>保持软件设计不退化的关键在于每次需求变更的设计，只有保证每次需求变更时做出正确的设计，才能保证软件以一种良性循环的方式不断维护下去。这种正确的设计方式就是“两顶帽子”。</strong></p>
<p>但是，在实践“两顶帽子”的过程中，比较困难的是第一步。在不添加新功能的前提下，如何重构代码，如何调整原有程序结构，以适应新功能，这是有难度的。很多时候，第一次变更、第二次变更、第三次变更，这些事情还能想清楚；但经历了第十次变更、第二十次变更、第三十次变更，这些事情就想不清楚了，设计开始迷失方向。</p>
<p>那么，<strong>有没有一种方法，让我们在第十次变更、第二十次变更、第三十次变更时，依然能够找到正确的设计呢？有，那就是“领域驱动设计”</strong>。</p>
<h3>保持软件质量：领域驱动</h3>
<p>前面谈到，软件的本质就是对真实世界的模拟。因此，我们会有一种想法，能不能将软件设计与真实世界对应起来，真实世界是什么样子，那么软件世界就怎么设计。如果是这样的话，那么在每次需求变更时，将变更还原到真实世界中，看看真实世界是什么样子的，根据真实世界进行变更。这样，日后不论怎么变更，经过多少轮变更，都按照这样的方法进行设计，就不会迷失方向，设计质量就可以得到保证，这就是“领域驱动设计”的思想。</p>
<p>那么，如何将真实世界与软件世界对应起来呢？这样的对应就包括以下三个方面的内容：</p>
<ul>
<li>真实世界有什么事物，软件世界就有什么对象；</li>
<li>真实世界中这些事物都有哪些行为，软件世界中这些对象就有哪些方法；</li>
<li>真实世界中这些事物间都有哪些关系，软件世界中这些对象间就有什么关联。</li>
</ul>
<p><img src="assets/CgqCHl-uXFKAM_mqAADumHk-Lio076.png" alt="图片5" /></p>
<p>真实世界与软件世界的对应图</p>
<p>在领域驱动设计中，就将以上三个对应，先做成一个领域模型，然后通过这个领域模型指导程序设计；在每次需求变更时，先将需求还原到领域模型中分析，根据领域模型背后的真实世界进行变更，然后根据领域模型的变更指导软件的变更，设计质量就可以得到提高。</p>
<h3>总结</h3>
<p>总之，软件发展的规律就是逐步由简单软件向复杂软件转变。简单软件有简单软件的设计，复杂软件有复杂软件的设计。因此，当软件由简单软件向复杂软件转变时，就需要通过两顶帽子适时地对程序结构进行调整，再实现新需求，只有这样才能保证软件不退化。然而，在变更的时候，如何调整代码以适应新的需求呢？</p>
<p>DDD 给了我们思路：在每次变更的时候，先回到领域模型，基于业务进行领域模型的变更。然后，再基于领域模型的变更，指导程序的变更。这样，不论经历多少次需求变更，始终能够保持设计质量不退化。这样的设计，才能保障系统始终在低成本的状态下，可持续地不断维护下去。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="00&#32;开篇词&#32;&#32;让我们把&#32;DDD&#32;的思想真正落地.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="02&#32;&#32;以电商支付功能为例演练&#32;DDD.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433dfd1e2f70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/DDD%20%E5%BE%AE%E6%9C%8D%E5%8A%A1%E8%90%BD%E5%9C%B0%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
