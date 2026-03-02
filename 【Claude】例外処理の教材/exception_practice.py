# 実践プログラム: 簡易ユーザー管理システム
# 例外処理を実際に使ってみる

"""
このプログラムの目的:
- try-except, raise, else, finally を実際に使う
- if文との使い分けを体験する
- 実用的なコードを書く練習
"""

import json
import os


class UserManager:
    """ユーザー管理システム"""
    
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = []
        self.load_users()
    
    def load_users(self):
        """ユーザーデータを読み込む"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            print(f"[INFO] {self.filename} が見つかりません。新規作成します。")
            self.users = []
        except json.JSONDecodeError as e:
            print(f"[ERROR] JSONファイルが壊れています: {e}")
            self.users = []
        else:
            print(f"[INFO] {len(self.users)}人のユーザーを読み込みました")
        finally:
            print("[INFO] 読み込み処理を完了しました")
    
    def save_users(self):
        """ユーザーデータを保存"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"[ERROR] 保存に失敗しました: {e}")
            return False
        else:
            print(f"[INFO] {len(self.users)}人のユーザーを保存しました")
            return True
        finally:
            print("[INFO] 保存処理を完了しました")
    
    def add_user(self, name, age, email):
        """ユーザーを追加"""
        # 入力値の検証（if文 + raise）
        if not isinstance(name, str) or not name.strip():
            raise ValueError("名前は空でない文字列である必要があります")
        
        if not isinstance(age, int):
            raise TypeError("年齢は整数である必要があります")
        
        if age < 0 or age > 150:
            raise ValueError("年齢は0から150の範囲で入力してください")
        
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("有効なメールアドレスを入力してください")
        
        # 重複チェック
        for user in self.users:
            if user['email'] == email:
                raise ValueError(f"メールアドレス {email} は既に登録されています")
        
        # ユーザー追加
        user = {
            "name": name,
            "age": age,
            "email": email
        }
        self.users.append(user)
        print(f"[SUCCESS] ユーザー {name} を追加しました")
        return user
    
    def find_user(self, email):
        """メールアドレスでユーザーを検索"""
        for user in self.users:
            if user['email'] == email:
                return user
        
        # 見つからない場合はNoneを返す（raiseではない）
        return None
    
    def update_age(self, email, new_age):
        """年齢を更新"""
        # 年齢の検証
        if not isinstance(new_age, int):
            raise TypeError("年齢は整数である必要があります")
        
        if new_age < 0 or new_age > 150:
            raise ValueError("年齢は0から150の範囲で入力してください")
        
        # ユーザーを検索
        user = self.find_user(email)
        
        if user is None:
            raise ValueError(f"メールアドレス {email} のユーザーが見つかりません")
        
        # 更新
        old_age = user['age']
        user['age'] = new_age
        print(f"[SUCCESS] {user['name']} の年齢を {old_age} → {new_age} に更新しました")
        return user
    
    def delete_user(self, email):
        """ユーザーを削除"""
        user = self.find_user(email)
        
        if user is None:
            raise ValueError(f"メールアドレス {email} のユーザーが見つかりません")
        
        self.users.remove(user)
        print(f"[SUCCESS] ユーザー {user['name']} を削除しました")
        return user
    
    def list_users(self):
        """全ユーザーを表示"""
        if not self.users:
            print("[INFO] 登録されているユーザーはいません")
            return
        
        print(f"\n{'='*50}")
        print(f"登録ユーザー一覧（{len(self.users)}人）")
        print("="*50)
        
        for i, user in enumerate(self.users, 1):
            print(f"{i}. {user['name']} ({user['age']}歳) - {user['email']}")
        
        print("="*50 + "\n")


# ============================================
# メインプログラム
# ============================================

def main():
    """メイン処理"""
    print("="*60)
    print("簡易ユーザー管理システム")
    print("="*60)
    print()
    
    # ユーザーマネージャーを初期化
    manager = UserManager()
    
    # --- テスト1: ユーザー追加（正常） ---
    print("\n[テスト1] ユーザー追加（正常）")
    print("-" * 60)
    try:
        manager.add_user("山田太郎", 25, "yamada@example.com")
        manager.add_user("佐藤花子", 30, "sato@example.com")
    except (ValueError, TypeError) as e:
        print(f"[ERROR] {e}")
    
    # --- テスト2: ユーザー追加（エラー） ---
    print("\n[テスト2] ユーザー追加（エラー）")
    print("-" * 60)
    
    # 名前が空
    try:
        manager.add_user("", 25, "empty@example.com")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # 年齢が文字列
    try:
        manager.add_user("田中一郎", "25", "tanaka@example.com")
    except TypeError as e:
        print(f"[ERROR] {e}")
    
    # 年齢が範囲外
    try:
        manager.add_user("鈴木二郎", 200, "suzuki@example.com")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # メールアドレスが不正
    try:
        manager.add_user("高橋三郎", 25, "invalid-email")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # 重複したメールアドレス
    try:
        manager.add_user("山田次郎", 28, "yamada@example.com")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # --- テスト3: ユーザー一覧表示 ---
    print("\n[テスト3] ユーザー一覧")
    print("-" * 60)
    manager.list_users()
    
    # --- テスト4: ユーザー検索 ---
    print("\n[テスト4] ユーザー検索")
    print("-" * 60)
    
    user = manager.find_user("yamada@example.com")
    if user:
        print(f"[SUCCESS] ユーザーが見つかりました: {user}")
    else:
        print("[INFO] ユーザーが見つかりませんでした")
    
    user = manager.find_user("notfound@example.com")
    if user:
        print(f"[SUCCESS] ユーザーが見つかりました: {user}")
    else:
        print("[INFO] ユーザーが見つかりませんでした")
    
    # --- テスト5: 年齢更新（正常） ---
    print("\n[テスト5] 年齢更新（正常）")
    print("-" * 60)
    try:
        manager.update_age("yamada@example.com", 26)
    except (ValueError, TypeError) as e:
        print(f"[ERROR] {e}")
    
    # --- テスト6: 年齢更新（エラー） ---
    print("\n[テスト6] 年齢更新（エラー）")
    print("-" * 60)
    
    # 存在しないユーザー
    try:
        manager.update_age("notfound@example.com", 30)
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # 年齢が不正
    try:
        manager.update_age("yamada@example.com", -5)
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # --- テスト7: ユーザー削除 ---
    print("\n[テスト7] ユーザー削除")
    print("-" * 60)
    try:
        manager.delete_user("sato@example.com")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # 存在しないユーザーを削除
    try:
        manager.delete_user("notfound@example.com")
    except ValueError as e:
        print(f"[ERROR] {e}")
    
    # --- テスト8: 最終的なユーザー一覧 ---
    print("\n[テスト8] 最終的なユーザー一覧")
    print("-" * 60)
    manager.list_users()
    
    # --- テスト9: データ保存 ---
    print("\n[テスト9] データ保存")
    print("-" * 60)
    manager.save_users()
    
    # --- クリーンアップ ---
    print("\n[クリーンアップ]")
    print("-" * 60)
    if os.path.exists("users.json"):
        os.remove("users.json")
        print("[INFO] テストファイルを削除しました")
    
    print("\n" + "="*60)
    print("全てのテストが完了しました！")
    print("="*60)


# ============================================
# 学んだポイントのまとめ
# ============================================

def print_lessons():
    """このプログラムから学べること"""
    print("\n" + "="*60)
    print("このプログラムから学べること")
    print("="*60)
    
    lessons = """
1. try-except-else-finally の使い方
   - load_users(): FileNotFoundError と JSONDecodeError
   - else: 正常時の処理
   - finally: 必ず実行するログ出力

2. raise を使うシーン
   - add_user(): 入力値の検証
   - update_age(): 年齢の検証
   - delete_user(): ユーザーが見つからない

3. if文 との使い分け
   - 型チェック: if + raise
   - ファイル操作: try-except
   - 検索結果: Noneを返す（raiseしない）

4. 複数の例外をキャッチ
   - except (ValueError, TypeError) as e:
   - 同じ処理で済む場合はまとめる

5. as e でエラー情報を取得
   - エラーメッセージをログに出力
   - ユーザーに分かりやすく伝える

6. 実践的なパターン
   - 入力値の検証: if + raise
   - ファイル操作: try-except-finally
   - データの検索: Noneを返す
   - 更新・削除: raiseでエラー通知
"""
    
    print(lessons)


if __name__ == "__main__":
    main()
    print_lessons()
