<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11 聚合：聚合查询之Metric聚合详解.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    <a class="current-tab" href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>
                    

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>11 聚合：聚合查询之Metric聚合详解</h1>
<h2>如何理解metric聚合</h2>
<blockquote>
<p>在[bucket聚合]中，我画了一张图辅助你构筑体系，那么metric聚合又如何理解呢？</p>
</blockquote>
<p>如果你直接去看官方文档，大概也有十几种：</p>
<p><img src="assets/es-agg-metric-1.png" alt="img" /></p>
<blockquote>
<p>那么metric聚合又如何理解呢？我认为从两个角度：</p>
</blockquote>
<ul>
<li><strong>从分类看</strong>：Metric聚合分析分为<strong>单值分析</strong>和<strong>多值分析</strong>两类</li>
<li><strong>从功能看</strong>：根据具体的应用场景设计了一些分析api, 比如地理位置，百分数等等</li>
</ul>
<blockquote>
<p>融合上述两个方面，我们可以梳理出大致的一个mind图：</p>
</blockquote>
<ul>
<li>
<p>单值分析</p>
<p>: 只输出一个分析结果</p>
<ul>
<li>标准stat型
<ul>
<li><code>avg</code> 平均值</li>
<li><code>max</code> 最大值</li>
<li><code>min</code> 最小值</li>
<li><code>sum</code> 和</li>
<li><code>value_count</code> 数量</li>
</ul>
</li>
<li>其它类型
<ul>
<li><code>cardinality</code> 基数（distinct去重）</li>
<li><code>weighted_avg</code> 带权重的avg</li>
<li><code>median_absolute_deviation</code> 中位值</li>
</ul>
</li>
</ul>
</li>
<li>
<p>多值分析</p>
<p>: 单值之外的</p>
<ul>
<li>stats型
<ul>
<li><code>stats</code> 包含avg,max,min,sum和count</li>
<li><code>matrix_stats</code> 针对矩阵模型</li>
<li><code>extended_stats</code></li>
<li><code>string_stats</code> 针对字符串</li>
</ul>
</li>
<li>百分数型
<ul>
<li><code>percentiles</code> 百分数范围</li>
<li><code>percentile_ranks</code> 百分数排行</li>
</ul>
</li>
<li>地理位置型
<ul>
<li><code>geo_bounds</code> Geo bounds</li>
<li><code>geo_centroid</code> Geo-centroid</li>
<li><code>geo_line</code> Geo-Line</li>
</ul>
</li>
<li>Top型
<ul>
<li><code>top_hits</code> 分桶后的top hits</li>
<li><code>top_metrics</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<p><strong>通过上述列表（我就不画图了），我们构筑的体系是基于分类和功能，而不是具体的项（比如avg,percentiles...)；这是不同的认知维度: 具体的项是碎片化，分类和功能这种是你需要构筑的体系</strong>。@pdai</p>
</blockquote>
<h2>单值分析: 标准stat类型</h2>
<h3><code>avg</code> 平均值</h3>
<p>计算班级的平均分</p>
<pre><code class="language-bash">POST /exams/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;avg_grade&quot;: { &quot;avg&quot;: { &quot;field&quot;: &quot;grade&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;avg_grade&quot;: {
      &quot;value&quot;: 75.0
    }
  }
}
</code></pre>
<h3><code>max</code> 最大值</h3>
<p>计算销售最高价</p>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;max_price&quot;: { &quot;max&quot;: { &quot;field&quot;: &quot;price&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
      &quot;max_price&quot;: {
          &quot;value&quot;: 200.0
      }
  }
}
</code></pre>
<h3><code>min</code> 最小值</h3>
<p>计算销售最低价</p>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;min_price&quot;: { &quot;min&quot;: { &quot;field&quot;: &quot;price&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...

  &quot;aggregations&quot;: {
    &quot;min_price&quot;: {
      &quot;value&quot;: 10.0
    }
  }
}
</code></pre>
<h3><code>sum</code> 和</h3>
<p>计算销售总价</p>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;query&quot;: {
    &quot;constant_score&quot;: {
      &quot;filter&quot;: {
        &quot;match&quot;: { &quot;type&quot;: &quot;hat&quot; }
      }
    }
  },
  &quot;aggs&quot;: {
    &quot;hat_prices&quot;: { &quot;sum&quot;: { &quot;field&quot;: &quot;price&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;hat_prices&quot;: {
      &quot;value&quot;: 450.0
    }
  }
}
</code></pre>
<h3><code>value_count</code> 数量</h3>
<p>销售数量统计</p>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;aggs&quot; : {
    &quot;types_count&quot; : { &quot;value_count&quot; : { &quot;field&quot; : &quot;type&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;types_count&quot;: {
      &quot;value&quot;: 7
    }
  }
}
</code></pre>
<h2>单值分析: 其它类型</h2>
<h3><code>weighted_avg</code> 带权重的avg</h3>
<pre><code class="language-bash">POST /exams/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;weighted_grade&quot;: {
      &quot;weighted_avg&quot;: {
        &quot;value&quot;: {
          &quot;field&quot;: &quot;grade&quot;
        },
        &quot;weight&quot;: {
          &quot;field&quot;: &quot;weight&quot;
        }
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;weighted_grade&quot;: {
      &quot;value&quot;: 70.0
    }
  }
}
</code></pre>
<h3><code>cardinality</code> 基数（distinct去重）</h3>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;type_count&quot;: {
      &quot;cardinality&quot;: {
        &quot;field&quot;: &quot;type&quot;
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;type_count&quot;: {
      &quot;value&quot;: 3
    }
  }
}
</code></pre>
<h3><code>median_absolute_deviation</code> 中位值</h3>
<pre><code class="language-bash">GET reviews/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;review_average&quot;: {
      &quot;avg&quot;: {
        &quot;field&quot;: &quot;rating&quot;
      }
    },
    &quot;review_variability&quot;: {
      &quot;median_absolute_deviation&quot;: {
        &quot;field&quot;: &quot;rating&quot; 
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;review_average&quot;: {
      &quot;value&quot;: 3.0
    },
    &quot;review_variability&quot;: {
      &quot;value&quot;: 2.0
    }
  }
}
</code></pre>
<h2>非单值分析：stats型</h2>
<h3><code>stats</code> 包含avg,max,min,sum和count</h3>
<pre><code class="language-bash">POST /exams/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;grades_stats&quot;: { &quot;stats&quot;: { &quot;field&quot;: &quot;grade&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...

  &quot;aggregations&quot;: {
    &quot;grades_stats&quot;: {
      &quot;count&quot;: 2,
      &quot;min&quot;: 50.0,
      &quot;max&quot;: 100.0,
      &quot;avg&quot;: 75.0,
      &quot;sum&quot;: 150.0
    }
  }
}
</code></pre>
<h3><code>matrix_stats</code> 针对矩阵模型</h3>
<p>以下示例说明了使用矩阵统计量来描述收入与贫困之间的关系。</p>
<pre><code class="language-bash">GET /_search
{
  &quot;aggs&quot;: {
    &quot;statistics&quot;: {
      &quot;matrix_stats&quot;: {
        &quot;fields&quot;: [ &quot;poverty&quot;, &quot;income&quot; ]
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...
  &quot;aggregations&quot;: {
    &quot;statistics&quot;: {
      &quot;doc_count&quot;: 50,
      &quot;fields&quot;: [ {
          &quot;name&quot;: &quot;income&quot;,
          &quot;count&quot;: 50,
          &quot;mean&quot;: 51985.1,
          &quot;variance&quot;: 7.383377037755103E7,
          &quot;skewness&quot;: 0.5595114003506483,
          &quot;kurtosis&quot;: 2.5692365287787124,
          &quot;covariance&quot;: {
            &quot;income&quot;: 7.383377037755103E7,
            &quot;poverty&quot;: -21093.65836734694
          },
          &quot;correlation&quot;: {
            &quot;income&quot;: 1.0,
            &quot;poverty&quot;: -0.8352655256272504
          }
        }, {
          &quot;name&quot;: &quot;poverty&quot;,
          &quot;count&quot;: 50,
          &quot;mean&quot;: 12.732000000000001,
          &quot;variance&quot;: 8.637730612244896,
          &quot;skewness&quot;: 0.4516049811903419,
          &quot;kurtosis&quot;: 2.8615929677997767,
          &quot;covariance&quot;: {
            &quot;income&quot;: -21093.65836734694,
            &quot;poverty&quot;: 8.637730612244896
          },
          &quot;correlation&quot;: {
            &quot;income&quot;: -0.8352655256272504,
            &quot;poverty&quot;: 1.0
          }
        } ]
    }
  }
}
</code></pre>
<h3><code>extended_stats</code></h3>
<p>根据从汇总文档中提取的数值计算统计信息。</p>
<pre><code class="language-bash">GET /exams/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;grades_stats&quot;: { &quot;extended_stats&quot;: { &quot;field&quot;: &quot;grade&quot; } }
  }
}
</code></pre>
<p>上面的汇总计算了所有文档的成绩统计信息。聚合类型为extended_stats，并且字段设置定义将在其上计算统计信息的文档的数字字段。</p>
<pre><code class="language-bash">{
  ...

  &quot;aggregations&quot;: {
    &quot;grades_stats&quot;: {
      &quot;count&quot;: 2,
      &quot;min&quot;: 50.0,
      &quot;max&quot;: 100.0,
      &quot;avg&quot;: 75.0,
      &quot;sum&quot;: 150.0,
      &quot;sum_of_squares&quot;: 12500.0,
      &quot;variance&quot;: 625.0,
      &quot;variance_population&quot;: 625.0,
      &quot;variance_sampling&quot;: 1250.0,
      &quot;std_deviation&quot;: 25.0,
      &quot;std_deviation_population&quot;: 25.0,
      &quot;std_deviation_sampling&quot;: 35.35533905932738,
      &quot;std_deviation_bounds&quot;: {
        &quot;upper&quot;: 125.0,
        &quot;lower&quot;: 25.0,
        &quot;upper_population&quot;: 125.0,
        &quot;lower_population&quot;: 25.0,
        &quot;upper_sampling&quot;: 145.71067811865476,
        &quot;lower_sampling&quot;: 4.289321881345245
      }
    }
  }
}
</code></pre>
<h3><code>string_stats</code> 针对字符串</h3>
<p>用于计算从聚合文档中提取的字符串值的统计信息。这些值可以从特定的关键字字段中检索。</p>
<pre><code class="language-bash">POST /my-index-000001/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;message_stats&quot;: { &quot;string_stats&quot;: { &quot;field&quot;: &quot;message.keyword&quot; } }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...

  &quot;aggregations&quot;: {
    &quot;message_stats&quot;: {
      &quot;count&quot;: 5,
      &quot;min_length&quot;: 24,
      &quot;max_length&quot;: 30,
      &quot;avg_length&quot;: 28.8,
      &quot;entropy&quot;: 3.94617750050791
    }
  }
}
</code></pre>
<h2>非单值分析：百分数型</h2>
<h3><code>percentiles</code> 百分数范围</h3>
<p>针对从聚合文档中提取的数值计算一个或多个百分位数。</p>
<pre><code class="language-bash">GET latency/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;load_time_outlier&quot;: {
      &quot;percentiles&quot;: {
        &quot;field&quot;: &quot;load_time&quot; 
      }
    }
  }
}
</code></pre>
<p>默认情况下，百分位度量标准将生成一定范围的百分位：[1，5，25，50，75，95，99]。</p>
<pre><code class="language-bash">{
  ...

 &quot;aggregations&quot;: {
    &quot;load_time_outlier&quot;: {
      &quot;values&quot;: {
        &quot;1.0&quot;: 5.0,
        &quot;5.0&quot;: 25.0,
        &quot;25.0&quot;: 165.0,
        &quot;50.0&quot;: 445.0,
        &quot;75.0&quot;: 725.0,
        &quot;95.0&quot;: 945.0,
        &quot;99.0&quot;: 985.0
      }
    }
  }
}
</code></pre>
<h3><code>percentile_ranks</code> 百分数排行</h3>
<p>根据从汇总文档中提取的数值计算一个或多个百分位等级。</p>
<pre><code class="language-bash">GET latency/_search
{
  &quot;size&quot;: 0,
  &quot;aggs&quot;: {
    &quot;load_time_ranks&quot;: {
      &quot;percentile_ranks&quot;: {
        &quot;field&quot;: &quot;load_time&quot;,   
        &quot;values&quot;: [ 500, 600 ]
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-bash">{
  ...

 &quot;aggregations&quot;: {
    &quot;load_time_ranks&quot;: {
      &quot;values&quot;: {
        &quot;500.0&quot;: 90.01,
        &quot;600.0&quot;: 100.0
      }
    }
  }
}
</code></pre>
<p>上述结果表示90.01％的页面加载在500ms内完成，而100％的页面加载在600ms内完成。</p>
<h2>非单值分析：地理位置型</h2>
<h3><code>geo_bounds</code> Geo bounds</h3>
<pre><code class="language-bash">PUT /museums
{
  &quot;mappings&quot;: {
    &quot;properties&quot;: {
      &quot;location&quot;: {
        &quot;type&quot;: &quot;geo_point&quot;
      }
    }
  }
}

POST /museums/_bulk?refresh
{&quot;index&quot;:{&quot;_id&quot;:1}}
{&quot;location&quot;: &quot;52.374081,4.912350&quot;, &quot;name&quot;: &quot;NEMO Science Museum&quot;}
{&quot;index&quot;:{&quot;_id&quot;:2}}
{&quot;location&quot;: &quot;52.369219,4.901618&quot;, &quot;name&quot;: &quot;Museum Het Rembrandthuis&quot;}
{&quot;index&quot;:{&quot;_id&quot;:3}}
{&quot;location&quot;: &quot;52.371667,4.914722&quot;, &quot;name&quot;: &quot;Nederlands Scheepvaartmuseum&quot;}
{&quot;index&quot;:{&quot;_id&quot;:4}}
{&quot;location&quot;: &quot;51.222900,4.405200&quot;, &quot;name&quot;: &quot;Letterenhuis&quot;}
{&quot;index&quot;:{&quot;_id&quot;:5}}
{&quot;location&quot;: &quot;48.861111,2.336389&quot;, &quot;name&quot;: &quot;Musée du Louvre&quot;}
{&quot;index&quot;:{&quot;_id&quot;:6}}
{&quot;location&quot;: &quot;48.860000,2.327000&quot;, &quot;name&quot;: &quot;Musée d'Orsay&quot;}

POST /museums/_search?size=0
{
  &quot;query&quot;: {
    &quot;match&quot;: { &quot;name&quot;: &quot;musée&quot; }
  },
  &quot;aggs&quot;: {
    &quot;viewport&quot;: {
      &quot;geo_bounds&quot;: {
        &quot;field&quot;: &quot;location&quot;,    
        &quot;wrap_longitude&quot;: true  
      }
    }
  }
}
</code></pre>
<p>上面的汇总展示了如何针对具有商店业务类型的所有文档计算位置字段的边界框</p>
<pre><code class="language-json">{
  ...
  &quot;aggregations&quot;: {
    &quot;viewport&quot;: {
      &quot;bounds&quot;: {
        &quot;top_left&quot;: {
          &quot;lat&quot;: 48.86111099738628,
          &quot;lon&quot;: 2.3269999679178
        },
        &quot;bottom_right&quot;: {
          &quot;lat&quot;: 48.85999997612089,
          &quot;lon&quot;: 2.3363889567553997
        }
      }
    }
  }
}
</code></pre>
<h3><code>geo_centroid</code> Geo-centroid</h3>
<pre><code class="language-bash">PUT /museums
{
  &quot;mappings&quot;: {
    &quot;properties&quot;: {
      &quot;location&quot;: {
        &quot;type&quot;: &quot;geo_point&quot;
      }
    }
  }
}

POST /museums/_bulk?refresh
{&quot;index&quot;:{&quot;_id&quot;:1}}
{&quot;location&quot;: &quot;52.374081,4.912350&quot;, &quot;city&quot;: &quot;Amsterdam&quot;, &quot;name&quot;: &quot;NEMO Science Museum&quot;}
{&quot;index&quot;:{&quot;_id&quot;:2}}
{&quot;location&quot;: &quot;52.369219,4.901618&quot;, &quot;city&quot;: &quot;Amsterdam&quot;, &quot;name&quot;: &quot;Museum Het Rembrandthuis&quot;}
{&quot;index&quot;:{&quot;_id&quot;:3}}
{&quot;location&quot;: &quot;52.371667,4.914722&quot;, &quot;city&quot;: &quot;Amsterdam&quot;, &quot;name&quot;: &quot;Nederlands Scheepvaartmuseum&quot;}
{&quot;index&quot;:{&quot;_id&quot;:4}}
{&quot;location&quot;: &quot;51.222900,4.405200&quot;, &quot;city&quot;: &quot;Antwerp&quot;, &quot;name&quot;: &quot;Letterenhuis&quot;}
{&quot;index&quot;:{&quot;_id&quot;:5}}
{&quot;location&quot;: &quot;48.861111,2.336389&quot;, &quot;city&quot;: &quot;Paris&quot;, &quot;name&quot;: &quot;Musée du Louvre&quot;}
{&quot;index&quot;:{&quot;_id&quot;:6}}
{&quot;location&quot;: &quot;48.860000,2.327000&quot;, &quot;city&quot;: &quot;Paris&quot;, &quot;name&quot;: &quot;Musée d'Orsay&quot;}

POST /museums/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;centroid&quot;: {
      &quot;geo_centroid&quot;: {
        &quot;field&quot;: &quot;location&quot; 
      }
    }
  }
}
</code></pre>
<p>上面的汇总显示了如何针对所有具有犯罪类型的盗窃文件计算位置字段的质心。</p>
<pre><code class="language-json">{
  ...
  &quot;aggregations&quot;: {
    &quot;centroid&quot;: {
      &quot;location&quot;: {
        &quot;lat&quot;: 51.00982965203002,
        &quot;lon&quot;: 3.9662131341174245
      },
      &quot;count&quot;: 6
    }
  }
}
</code></pre>
<h3><code>geo_line</code> Geo-Line</h3>
<pre><code class="language-bash">PUT test
{
    &quot;mappings&quot;: {
        &quot;dynamic&quot;: &quot;strict&quot;,
        &quot;_source&quot;: {
            &quot;enabled&quot;: false
        },
        &quot;properties&quot;: {
            &quot;my_location&quot;: {
                &quot;type&quot;: &quot;geo_point&quot;
            },
            &quot;group&quot;: {
                &quot;type&quot;: &quot;keyword&quot;
            },
            &quot;@timestamp&quot;: {
                &quot;type&quot;: &quot;date&quot;
            }
        }
    }
}

POST /test/_bulk?refresh
{&quot;index&quot;: {}}
{&quot;my_location&quot;: {&quot;lat&quot;:37.3450570, &quot;lon&quot;: -122.0499820}, &quot;@timestamp&quot;: &quot;2013-09-06T16:00:36&quot;}
{&quot;index&quot;: {}}
{&quot;my_location&quot;: {&quot;lat&quot;: 37.3451320, &quot;lon&quot;: -122.0499820}, &quot;@timestamp&quot;: &quot;2013-09-06T16:00:37Z&quot;}
{&quot;index&quot;: {}}
{&quot;my_location&quot;: {&quot;lat&quot;: 37.349283, &quot;lon&quot;: -122.0505010}, &quot;@timestamp&quot;: &quot;2013-09-06T16:00:37Z&quot;}

POST /test/_search?filter_path=aggregations
{
  &quot;aggs&quot;: {
    &quot;line&quot;: {
      &quot;geo_line&quot;: {
        &quot;point&quot;: {&quot;field&quot;: &quot;my_location&quot;},
        &quot;sort&quot;: {&quot;field&quot;: &quot;@timestamp&quot;}
      }
    }
  }
}
</code></pre>
<p>将存储桶中的所有geo_point值聚合到由所选排序字段排序的LineString中。</p>
<pre><code class="language-json">{
  &quot;aggregations&quot;: {
    &quot;line&quot;: {
      &quot;type&quot; : &quot;Feature&quot;,
      &quot;geometry&quot; : {
        &quot;type&quot; : &quot;LineString&quot;,
        &quot;coordinates&quot; : [
          [
            -122.049982,
            37.345057
          ],
          [
            -122.050501,
            37.349283
          ],
          [
            -122.049982,
            37.345132
          ]
        ]
      },
      &quot;properties&quot; : {
        &quot;complete&quot; : true
      }
    }
  }
}
</code></pre>
<h2>非单值分析：Top型</h2>
<h3><code>top_hits</code> 分桶后的top hits</h3>
<pre><code class="language-bash">POST /sales/_search?size=0
{
  &quot;aggs&quot;: {
    &quot;top_tags&quot;: {
      &quot;terms&quot;: {
        &quot;field&quot;: &quot;type&quot;,
        &quot;size&quot;: 3
      },
      &quot;aggs&quot;: {
        &quot;top_sales_hits&quot;: {
          &quot;top_hits&quot;: {
            &quot;sort&quot;: [
              {
                &quot;date&quot;: {
                  &quot;order&quot;: &quot;desc&quot;
                }
              }
            ],
            &quot;_source&quot;: {
              &quot;includes&quot;: [ &quot;date&quot;, &quot;price&quot; ]
            },
            &quot;size&quot;: 1
          }
        }
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-json">{
  ...
  &quot;aggregations&quot;: {
    &quot;top_tags&quot;: {
       &quot;doc_count_error_upper_bound&quot;: 0,
       &quot;sum_other_doc_count&quot;: 0,
       &quot;buckets&quot;: [
          {
             &quot;key&quot;: &quot;hat&quot;,
             &quot;doc_count&quot;: 3,
             &quot;top_sales_hits&quot;: {
                &quot;hits&quot;: {
                   &quot;total&quot; : {
                       &quot;value&quot;: 3,
                       &quot;relation&quot;: &quot;eq&quot;
                   },
                   &quot;max_score&quot;: null,
                   &quot;hits&quot;: [
                      {
                         &quot;_index&quot;: &quot;sales&quot;,
                         &quot;_type&quot;: &quot;_doc&quot;,
                         &quot;_id&quot;: &quot;AVnNBmauCQpcRyxw6ChK&quot;,
                         &quot;_source&quot;: {
                            &quot;date&quot;: &quot;2015/03/01 00:00:00&quot;,
                            &quot;price&quot;: 200
                         },
                         &quot;sort&quot;: [
                            1425168000000
                         ],
                         &quot;_score&quot;: null
                      }
                   ]
                }
             }
          },
          {
             &quot;key&quot;: &quot;t-shirt&quot;,
             &quot;doc_count&quot;: 3,
             &quot;top_sales_hits&quot;: {
                &quot;hits&quot;: {
                   &quot;total&quot; : {
                       &quot;value&quot;: 3,
                       &quot;relation&quot;: &quot;eq&quot;
                   },
                   &quot;max_score&quot;: null,
                   &quot;hits&quot;: [
                      {
                         &quot;_index&quot;: &quot;sales&quot;,
                         &quot;_type&quot;: &quot;_doc&quot;,
                         &quot;_id&quot;: &quot;AVnNBmauCQpcRyxw6ChL&quot;,
                         &quot;_source&quot;: {
                            &quot;date&quot;: &quot;2015/03/01 00:00:00&quot;,
                            &quot;price&quot;: 175
                         },
                         &quot;sort&quot;: [
                            1425168000000
                         ],
                         &quot;_score&quot;: null
                      }
                   ]
                }
             }
          },
          {
             &quot;key&quot;: &quot;bag&quot;,
             &quot;doc_count&quot;: 1,
             &quot;top_sales_hits&quot;: {
                &quot;hits&quot;: {
                   &quot;total&quot; : {
                       &quot;value&quot;: 1,
                       &quot;relation&quot;: &quot;eq&quot;
                   },
                   &quot;max_score&quot;: null,
                   &quot;hits&quot;: [
                      {
                         &quot;_index&quot;: &quot;sales&quot;,
                         &quot;_type&quot;: &quot;_doc&quot;,
                         &quot;_id&quot;: &quot;AVnNBmatCQpcRyxw6ChH&quot;,
                         &quot;_source&quot;: {
                            &quot;date&quot;: &quot;2015/01/01 00:00:00&quot;,
                            &quot;price&quot;: 150
                         },
                         &quot;sort&quot;: [
                            1420070400000
                         ],
                         &quot;_score&quot;: null
                      }
                   ]
                }
             }
          }
       ]
    }
  }
}
</code></pre>
<h3><code>top_metrics</code></h3>
<pre><code class="language-bash">POST /test/_bulk?refresh
{&quot;index&quot;: {}}
{&quot;s&quot;: 1, &quot;m&quot;: 3.1415}
{&quot;index&quot;: {}}
{&quot;s&quot;: 2, &quot;m&quot;: 1.0}
{&quot;index&quot;: {}}
{&quot;s&quot;: 3, &quot;m&quot;: 2.71828}
POST /test/_search?filter_path=aggregations
{
  &quot;aggs&quot;: {
    &quot;tm&quot;: {
      &quot;top_metrics&quot;: {
        &quot;metrics&quot;: {&quot;field&quot;: &quot;m&quot;},
        &quot;sort&quot;: {&quot;s&quot;: &quot;desc&quot;}
      }
    }
  }
}
</code></pre>
<p>返回</p>
<pre><code class="language-json">{
  &quot;aggregations&quot;: {
    &quot;tm&quot;: {
      &quot;top&quot;: [ {&quot;sort&quot;: [3], &quot;metrics&quot;: {&quot;m&quot;: 2.718280076980591 } } ]
    }
  }
}
</code></pre>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4340383c6370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
