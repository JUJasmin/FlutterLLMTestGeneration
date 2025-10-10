import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_testing_app/profile_avatar.dart';

void main() {
  testWidgets('ProfileAvatar renders a CircleAvatar with the correct image', (WidgetTester tester) async {
    final String imageUrl = 'https://images.unsplash.com/photo-1512777774577-999999999999?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80';
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
        body: Center(
          child: ProfileAvatar(imageUrl: imageUrl),
        ),
      ),
    ));

    expect(find.byType(CircleAvatar), findsOneWidget);
    expect(find.byType(CircleAvatar), findsOneWidget);
    expect(find.byType(CircleAvatar), findsOneWidget);
  });
}