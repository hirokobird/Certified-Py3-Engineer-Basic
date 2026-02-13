#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ログ分析ツール - Pythonエンジニア基礎検定学習用
以下の項目を学習するための教材プログラム：
1. for文やif文で使うbreakとcontinue
2. *args, **kwargs（可変長引数とアンパック）
3. 比較演算子の短絡評価
4. raise文（カスタム例外）
5. argparse/ArgumentParser
"""

import argparse
from typing import List, Dict


# ================================================================================
# ④ raise文：カスタム例外クラスの定義
# ================================================================================
class LogAnalyzerError(Exception):
    """ログ分析ツール専用の例外クラス"""
    pass


class LogFileNotFoundError(LogAnalyzerError):
    """ログファイルが見つからない場合の例外"""
    pass


class InvalidLogFormatError(LogAnalyzerError):
    """ログフォーマットが不正な場合の例外"""
    pass


# ================================================================================
# ③ *args, **kwargs：可変長引数を使った関数
# ================================================================================
def print_log_info(*messages, **options):
    """
    ログ情報を表示する関数
    
    Args:
        *messages: 可変長位置引数。複数のメッセージを受け取る
        **options: 可変長キーワード引数。表示オプションを受け取る
    
    学習ポイント：
    - *messages は任意の数の位置引数をタプルとして受け取る
    - **options は任意の数のキーワード引数を辞書として受け取る
    """
    # オプションから表示設定を取得（デフォルト値を設定）
    prefix = options.get('prefix', '[INFO]')
    separator = options.get('separator', ' | ')
    uppercase = options.get('uppercase', False)
    
    # メッセージを結合
    message = separator.join(str(msg) for msg in messages)
    
    # 大文字変換オプション
    if uppercase:
        message = message.upper()
    
    print(f"{prefix} {message}")


def analyze_logs(*log_files, **filters):
    """
    複数のログファイルを分析する関数
    
    Args:
        *log_files: 分析対象のログファイルパス（複数指定可能）
        **filters: フィルタリング条件（level, keyword など）
    
    Returns:
        dict: 分析結果
    """
    results = {
        'total_lines': 0,
        'error_count': 0,
        'warning_count': 0,
        'info_count': 0,
        'matched_lines': []
    }
    
    # フィルタ条件を取得
    level_filter = filters.get('level', None)
    keyword_filter = filters.get('keyword', None)
    max_results = filters.get('max_results', None)
    
    # 各ログファイルを処理
    for log_file in log_files:
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                # ================================================================================
                # ② for文で使うbreakとcontinue
                # ================================================================================
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    
                    # 空行はスキップ（continue）
                    if not line:
                        continue
                    
                    results['total_lines'] += 1
                    
                    # ログレベルをカウント
                    if 'ERROR' in line:
                        results['error_count'] += 1
                    elif 'WARNING' in line:
                        results['warning_count'] += 1
                    elif 'INFO' in line:
                        results['info_count'] += 1
                    
                    # ================================================================================
                    # ⑤ 比較演算子の短絡評価
                    # ================================================================================
                    # level_filterがNoneでない場合のみ、かつ条件に合致する場合のみ処理
                    # 短絡評価：level_filterがNoneの場合、'in line'は評価されない
                    if level_filter and level_filter not in line:
                        continue
                    
                    # keyword_filterがNoneでない場合のみ、かつ条件に合致する場合のみ処理
                    # 短絡評価：keyword_filterがNoneの場合、'not in line'は評価されない
                    if keyword_filter and keyword_filter not in line:
                        continue
                    
                    # マッチした行を保存
                    results['matched_lines'].append({
                        'file': log_file,
                        'line_num': line_num,
                        'content': line
                    })
                    
                    # ================================================================================
                    # ② max_resultsに達したらループを抜ける（break）
                    # ================================================================================
                    # max_resultsがNoneでない場合のみ、かつ件数チェック（短絡評価）
                    if max_results and len(results['matched_lines']) >= max_results:
                        print(f"最大表示件数（{max_results}件）に達したため、処理を終了します")
                        break
        
        except FileNotFoundError:
            # ④ raise文：カスタム例外を発生させる
            raise LogFileNotFoundError(f"ログファイルが見つかりません: {log_file}")
        except Exception as e:
            raise LogAnalyzerError(f"ログファイルの読み込み中にエラーが発生しました: {e}")
    
    return results


def display_results(results: Dict, **display_options):
    """
    分析結果を表示する関数
    
    Args:
        results: analyze_logs関数の戻り値
        **display_options: 表示オプション（show_stats, show_lines など）
    """
    show_stats = display_options.get('show_stats', True)
    show_lines = display_options.get('show_lines', True)
    verbose = display_options.get('verbose', False)
    
    print("\n" + "=" * 60)
    print("ログ分析結果")
    print("=" * 60)
    
    if show_stats:
        print(f"\n【統計情報】")
        print(f"総行数: {results['total_lines']}")
        print(f"ERROR: {results['error_count']}")
        print(f"WARNING: {results['warning_count']}")
        print(f"INFO: {results['info_count']}")
        print(f"条件に一致した行数: {len(results['matched_lines'])}")
    
    if show_lines and results['matched_lines']:
        print(f"\n【該当ログ】")
        for match in results['matched_lines']:
            if verbose:
                print(f"ファイル: {match['file']}, 行番号: {match['line_num']}")
                print(f"  {match['content']}")
            else:
                print(f"{match['content']}")
    
    print("=" * 60 + "\n")


# ================================================================================
# ⑦ argparse/ArgumentParser：コマンドライン引数の処理
# ================================================================================
def main():
    """メイン関数：コマンドライン引数を解析してログ分析を実行"""
    
    # ArgumentParserオブジェクトを作成
    parser = argparse.ArgumentParser(
        description='ログファイルを分析するツール（Pythonエンジニア基礎検定学習用）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 基本的な使い方
  python log_analyzer.py sample_access.log
  
  # ERRORレベルのみ表示
  python log_analyzer.py sample_access.log --level ERROR
  
  # 特定のキーワードを含む行を検索
  python log_analyzer.py sample_access.log --keyword "Database"
  
  # 複数のフィルタを組み合わせ
  python log_analyzer.py sample_access.log --level ERROR --keyword "connection" --max 5
  
  # 複数のログファイルを分析
  python log_analyzer.py log1.log log2.log log3.log
        """
    )
    
    # 位置引数：ログファイル（複数指定可能）
    parser.add_argument(
        'logfiles',
        nargs='+',  # 1つ以上の引数を受け取る
        help='分析対象のログファイルパス（複数指定可能）'
    )
    
    # オプション引数：ログレベルフィルタ
    parser.add_argument(
        '-l', '--level',
        choices=['ERROR', 'WARNING', 'INFO'],
        help='特定のログレベルのみ表示'
    )
    
    # オプション引数：キーワードフィルタ
    parser.add_argument(
        '-k', '--keyword',
        help='指定したキーワードを含む行のみ表示'
    )
    
    # オプション引数：最大表示件数
    parser.add_argument(
        '-m', '--max',
        type=int,
        help='最大表示件数を指定'
    )
    
    # オプション引数：統計情報のみ表示
    parser.add_argument(
        '-s', '--stats-only',
        action='store_true',
        help='統計情報のみ表示（該当ログは表示しない）'
    )
    
    # オプション引数：詳細表示
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='詳細情報を表示（ファイル名、行番号を含む）'
    )
    
    # 引数を解析
    args = parser.parse_args()
    
    try:
        # ================================================================================
        # ③ アンパック：辞書を**でキーワード引数として展開
        # ================================================================================
        # フィルタ条件を辞書にまとめる
        filters = {}
        if args.level:
            filters['level'] = args.level
        if args.keyword:
            filters['keyword'] = args.keyword
        if args.max:
            filters['max_results'] = args.max
        
        # *args.logfiles でリストをアンパック、**filters で辞書をアンパック
        print_log_info(
            "ログ分析を開始します",
            f"対象ファイル: {', '.join(args.logfiles)}",
            prefix="[START]",
            separator=" - "
        )
        
        # ログ分析を実行（アンパックを使用）
        results = analyze_logs(*args.logfiles, **filters)
        
        # 表示オプションを辞書にまとめる
        display_opts = {
            'show_stats': True,
            'show_lines': not args.stats_only,
            'verbose': args.verbose
        }
        
        # 結果を表示（アンパックを使用）
        display_results(results, **display_opts)
        
        print_log_info("ログ分析が完了しました", prefix="[END]")
    
    # ④ raise文：カスタム例外のキャッチと処理
    except LogFileNotFoundError as e:
        print(f"エラー: {e}")
        return 1
    except LogAnalyzerError as e:
        print(f"エラー: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n処理を中断しました")
        return 130
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
